from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg
import os

def divide_scene_from_all_videos(dir_path):
    files = os.listdir(dir_path)
    
    # エラーを起こした時、途中から読み込むためのコード
    print(files.index('75289802.mp4'))
    files = files[files.index('75289802.mp4'):]
    
    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        print(file_path)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.mp4', '.avi', '.mov')):
            scene_list = detect(file_path, AdaptiveDetector())
            split_video_ffmpeg(file_path, 
                            scene_list, 
                            output_file_template=f'{dir_path}/scenes/$VIDEO_NAME-$SCENE_NUMBER.mp4', 
                            show_progress=True,
                            )
            
input_path = '/Volumes/Steam SSD/videos'
divide_scene_from_all_videos(input_path)