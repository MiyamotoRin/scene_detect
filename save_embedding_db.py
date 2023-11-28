import os
from PIL import Image
import torch
import open_clip

import numpy as np
from usearch.index import Index, Matches

# Load the model and tokenizer from open_clip
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

# Define the directory path containing the images
directory_path = '/Volumes/Steam SSD/videos/thumbnails/'  # This path will need to be updated by the user

# List all image files in the specified directory
image_files = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# image_files = image_files[:50]

# Define Usearch index
index = Index(
    ndim=512, # Define the number of dimensions in input vectors
    metric='cos', # Choose 'l2sq', 'haversine' or other metric, default = 'ip'
    dtype='f32', # Quantize to 'f16' or 'i8' if needed, default = 'f32'
    connectivity=16, # How frequent should the connections in the graph be, optional
    expansion_add=128, # Control the recall of indexing, optional
    expansion_search=64, # Control the quality of search, optional
)

db_id = 0
# Process each image to embed and add to Usearch index
with torch.no_grad(), torch.cuda.amp.autocast():
    for image_path in image_files:
        image = preprocess(Image.open(image_path)).unsqueeze(0)
        image_features = model.encode_image(image)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        index.add(db_id, image_features.numpy()[0], log=True)
        db_id += 1

index.save('index.usearch')
