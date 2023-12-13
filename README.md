# scene_detect

動画からサムネを作るスクリプトです。
動画をシーンごとに分割するスクリプトもあります。

## 環境

- Python 3.12
- Poetry 1.7.0

## インストール方法

1. このリポジトリをクローンします。
2. 依存ファイルをインストールします。
```
pip install poetry
poetry install
```

## 使い方
- divide_scene.py \
    動画をシーンごとに分割する
- create_thumbnail.py \
    動画(シーン)のディレクトリからサムネを作成する
- make_embedding_db.py \
    サムネをembeddingに変換して、データベースに格納する
- make_sql_db.py \
    サムネのembeddingと動画のパスを紐づけるデータベースを作成する
- search_video.py \
    動画のパスを検索する