from thumbnail import generate_thumbnail
import os

# generate_thumbnail(input, output, options)

def create_thumbnails_for_all_videos(input_path, output_path, thumbnail_options):   
    # ディレクトリ内の全てのファイルを取得
    files = os.listdir(input_path)
    # ディレクトリ内の各ファイルに対して処理
    for file_name in files:
        # ファイルの完全なパスを生成
        file_path = os.path.join(input_path, file_name)
        
        # ファイルが動画ファイルかどうかをチェック（例: .mp4）
        if os.path.isfile(file_path) and file_path.lower().endswith(('.mp4', '.avi', '.mov')):
            # サムネイルの保存先パスを生成
            thumbnail_path = os.path.join(output_path, f'{os.path.splitext(file_name)[0]}.png')
            print(thumbnail_path)
            # サムネイルを生成
            generate_thumbnail(file_path, thumbnail_path, thumbnail_options)

if __name__ == '__main__':
    input_path = "/Volumes/Steam_SSD/videos/scenes"
    output_path = "/Volumes/Steam_SSD/videos/thumbnails"

    options = {
        'trim': False,
        'height': 300,
        'width': 300,
        'quality': 85,
        'type': 'thumbnail'
    }

    create_thumbnails_for_all_videos(input_path, output_path, options)
