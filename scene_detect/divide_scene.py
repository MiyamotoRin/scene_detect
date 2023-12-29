from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg
import os

def divide_scene_from_video(video_path):
    parent_directory, file_name = os.path.split(video_path)
    
    if os.path.isfile(video_path) and video_path.lower().endswith(('.mp4', '.avi', '.mov')):
        scene_list = detect(video_path, AdaptiveDetector())
        split_video_ffmpeg(video_path, 
                        scene_list, 
                        output_file_template=f'{parent_directory}/cuts/$VIDEO_NAME-C$SCENE_NUMBER.mp4', 
                        show_progress=True,
                        )

def divide_scene_from_all_videos(dir_path):
    files = os.listdir(dir_path)
    
    # エラーを起こした時、途中から読み込むためのコード
    # print(files.index('75289802.mp4'))
    # files = files[files.index('75289802.mp4'):]
    
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