from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg

scene_list = detect('sample.mp4', AdaptiveDetector())
split_video_ffmpeg('sample.mp4', 
                   scene_list, 
                   output_file_template='scenes/$VIDEO_NAME-Scene-$SCENE_NUMBER.mp4', 
                   show_progress=True,
                   )