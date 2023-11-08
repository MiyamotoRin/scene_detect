from thumbnail import generate_thumbnail
import os

# generate_thumbnail(input, output, options)

input_path = 'scenes/sample-Scene-028.mp4'

filename = os.path.basename(input_path)
basename, extension = os.path.splitext(filename)
output_dir = '/Users/techkidsschool/Desktop/scene_detect/thumbnails/'
output_path = output_dir + basename + '.png'
print(output_path)

options = {
	'trim': False,
	'height': 300,
	'width': 300,
	'quality': 85,
	'type': 'thumbnail'
}
generate_thumbnail(input_path, output_path, options)