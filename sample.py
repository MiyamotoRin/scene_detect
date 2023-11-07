from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg

scene_list = detect('ノスタルジックに浸る～四国村～ [5Xxtq6dkG4g].mp4', AdaptiveDetector())
print(scene_list)
split_video_ffmpeg('ノスタルジックに浸る～四国村～ [5Xxtq6dkG4g].mp4', scene_list)