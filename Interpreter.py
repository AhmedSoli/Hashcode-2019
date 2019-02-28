import logging

def parse(filePath: str):
	# read file
	logging.info(f"Working on file {filePath}")
	with open(filePath, 'r') as opened_file:
		i = 0
		# interprete the data
		photos = []
		for line in opened_file:
			if i == 0:
				number_of_photos = line.split(" ")[0]
				print(number_of_photos)
			else:
				photo = {}
				vals = line.split(' ')
				photo['direction'] = vals[0]
				vals[-1] = vals[-1].replace('\n','')
				photo['tags'] = vals[2:]
				photos.append(photo)
			i += 1
		# solve the data
	return photos
