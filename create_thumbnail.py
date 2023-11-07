from thumbnail import generate_thumbnail

# generate_thumbnail(input, output, options)

input_path = 'sample-Scene-028.mp4'

options = {
	'trim': False,
	'height': 300,
	'width': 300,
	'quality': 85,
	'type': 'thumbnail'
}
generate_thumbnail(input_path, './thumbnails/.png', options)