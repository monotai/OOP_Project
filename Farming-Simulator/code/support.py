import pygame

class SpriteSheet():
	def __init__(self, path):
		pygame.display.init()
		pygame.display.set_mode((1, 1), pygame.NOFRAME)  # Create a minimal display
		self.sheet = pygame.image.load(path).convert_alpha()
	
	def get_image(self, pos_2, size_2, scale_2, colour = None):
			image = pygame.Surface(size_2).convert_alpha()
			image.fill((0, 0, 0, 0))

			image.blit(self.sheet, (0, 0), (pos_2[0], pos_2[1], size_2[0], size_2[1]))
			image = pygame.transform.scale(image, scale_2)

			if colour is not None:
				image.set_colorkey(colour)

			return image

	def get_images_sheet(self, pos_2, frames_3, size_2, scale_2, colour = None):
		images = []
		maxIndex = frames_3[2]
		for i in range(frames_3[0]):
			for j in range(frames_3[1]):
				if maxIndex == 0:
					return images
				images.append(self.get_image((pos_2[0] + i * size_2[0], pos_2[1] + j * size_2[1]), size_2, scale_2, colour))
				maxIndex -= 1

		return images
	
	# data
	# {
	#     "type": {
	#         "pos": [x, y],
	#         "size": [w, h],
	#         "frames": [m, n]
	#     }
	# }
	# image is an rangtangle
	
	def get_all_sprites(self, data, scale_2, size_2 = None):
		imagesData = {}
		frames_3 = (data[typeSprite]["frames"][0], data[typeSprite]["frames"][1], data[typeSprite]["frames"][0]*data[typeSprite]["frames"][1])
		if size_2 is None:
			for typeSprite in data.keys():
				imagesData[typeSprite] = self.get_images_sheet(data[typeSprite]["pos"], frames_3, data[typeSprite]["size"], scale_2)
		else :
			for typeSprite in data.keys():
				imagesData[typeSprite] = self.get_images_sheet(data[typeSprite]["pos"], frames_3, size_2, scale_2)

		return imagesData
	# column : c
	# widthImage
	# size = [w, h]
	# grid = [g_x, g_y]
	# data 
	#{
	#   "type":{
	#		"index": i,
	#		"frames": f
	#	   }
	#}

	# grid is for sprite sheet in ragtangle form and column mean for divid sprite sheet from image
	def get_all_sprites_by_index(self, data, widthImage, grid, size ,scale, frames = None):
		imagesData = {}

		width = size[0]*grid[0]
		height = size[1]*grid[1]

		column = widthImage // width

		for typeSprite, dataSprite in data.items():
			pos = ((dataSprite["index"] % column) * width, (dataSprite["index"] // column) * height)

			# !!!!!!!!! I'm So tired !!!! for this
			current_frames = (grid[0], grid[1], frames) if frames is not None else (grid[0], grid[1], dataSprite["frames"])
			imagesData[typeSprite] = self.get_images_sheet(pos, current_frames, size, scale)



		return imagesData
		

	#data
	#{
	#	"typeData": {
	#			"key": value
	#			}
	#}
	# new data
	#{
	#	"typeData": {
	#				"addKey": newValue
	#				}
	#}
	# get
	#{
	#	"typeData": {
	#			"key": value,
	#			"new key": newValue
	#			}
	#}

def copy_json_by_key(data, copyData, key, copyKey):
	if len(copyData) == 0:
		for typeData in data.keys():
			copyData[typeData] = {}
			copyData[typeData][copyKey] = data[typeData][key] 
	else :
		for typeData in data.keys():
			copyData[typeData][copyKey] = data[typeData][key] 

# def json_insert(data, addData, addKey):

# 	for typeData in data.keys():
# 		if typeData in newData:
# 			typeData[newkey] = newData[typeData][addKey]
