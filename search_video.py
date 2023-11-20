import os
from PIL import Image
import torch
import open_clip

# Load the model and tokenizer from open_clip
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

# Define the directory path containing the images
directory_path = '/Volumes/Steam SSD/videos/thumbnails/'  # This path will need to be updated by the user

# List all image files in the specified directory
image_files = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Define the texts to compare with
texts = ["A man with a loaf of bread in his mouth is running."]
text_tokens = tokenizer(texts)

# Placeholder for the similarity scores and corresponding image paths
image_similarity = {text: [] for text in texts}

# Process each image and calculate similarity
with torch.no_grad(), torch.cuda.amp.autocast():
    text_features = model.encode_text(text_tokens)
    text_features /= text_features.norm(dim=-1, keepdim=True)

    for image_path in image_files:
        image = preprocess(Image.open(image_path)).unsqueeze(0)
        image_features = model.encode_image(image)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        similarity_scores = (100.0 * image_features @ text_features.T).softmax(dim=-1)

        # Update the image_similarity dictionary with the similarity scores
        for i, text in enumerate(texts):
            image_similarity[text].append((similarity_scores[0, i].item(), image_path))

# Sort the similarity scores for each text and get the top 5 images
top_images_per_text = {text: sorted(image_similarity[text], key=lambda x: x[0], reverse=True)[:5] for text in texts}

# Output the paths of the top 5 images for each input text
print(top_images_per_text)
