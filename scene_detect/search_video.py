import os
from PIL import Image
import torch
import open_clip
from usearch.index import Index, Matches

import sqlite3

def get_video_index(texts, db_path):
    # Load the model and tokenizer from open_clip
    model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
    tokenizer = open_clip.get_tokenizer('ViT-B-32')

    # Define the texts to compare with
    text_tokens = tokenizer(texts)

    # Load the Usearch index
    index = Index()
    # index.load('index.usearch')
    index = Index.restore(db_path, view=True)
    print(Index.metadata(db_path))

    # Process each image and calculate similarity
    with torch.no_grad(), torch.cuda.amp.autocast():
        text_features = model.encode_text(text_tokens)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        text_features = text_features.numpy()
        matches: Matches = index.search(text_features[0].flatten(), 3)
    
    return matches[0].key

def get_video_path(video_id, db_path):
    video_id += 1
    
    # データベースに接続する
    conn = sqlite3.connect(db_path)

    # カーソルオブジェクトを作成する
    cursor = conn.cursor()

    # SQLクエリを実行する
    cursor.execute('SELECT * FROM file_paths WHERE id=?', (video_id,))

    # 結果を取得する
    record = cursor.fetchone()

    # 接続を閉じる
    conn.close()
    
    return record[1]
    
if __name__ == '__main__':
    video_id = get_video_index(["A fire works in the sky"], 'index.usearch')
    path = get_video_path(video_id, 'file_paths.db')
    print(path)