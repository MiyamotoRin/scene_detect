from scene_detect.divide_scene import divide_scene_from_video
from scene_detect.create_thumbnail import create_thumbnails_for_all_videos

if __name__ == '__main__':
    # input = '/Volumes/muheS1T01/CondensedMovies/videos/2019/'
    # output = '/Volumes/muheS1T01/prj_rin_miyamoto_231228/thumbnails'
    # options = {
    #     'trim': False,
    #     'height': 300,
    #     'width': 300,
    #     'quality': 85,
    #     'type': 'thumbnail'
    # }
    # create_thumbnails_for_all_videos(input, output, options)
    
    # input = '/Volumes/muheS1T01/CondensedMovies/videos/2019/Les_Miserables_S34.mp4'
    # divide_scene_from_video(input)
    
    dir_path = '/Volumes/muheS1T01/CondensedMovies/videos/2019/'
    options = {
        'trim': False,
        'height': 300,
        'width': 300,
        'quality': 85,
        'type': 'thumbnail'
    }
    create_thumbnails_for_all_videos(dir_path+'cuts', dir_path+'thumbnails', options)