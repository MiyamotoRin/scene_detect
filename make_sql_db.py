import sqlite3
import os

# データベースの作成
conn = sqlite3.connect('file_paths.db')
c = conn.cursor()

# テーブルの作成
c.execute('''CREATE TABLE IF NOT EXISTS file_paths
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              path TEXT)''')

# ディレクトリ内のパスを取得してデータベースに格納
directory = '/Volumes/muheS1T01/videos/scenes/'
for root, dirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(root, file)
        c.execute("INSERT INTO file_paths (path) VALUES (?)", (path,))

# 変更をコミットして接続を閉じる
conn.commit()
conn.close()
