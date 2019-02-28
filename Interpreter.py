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
				logging.info(number_of_photos)
			else:
				photo = {}
				vals = line.split(' ')
				photo['direction'] = vals[0]
				vals[-1] = vals[-1].replace('\n','')
				photo['tags'] = set(vals[2:])
				photo['id'] = i - 1
				photos.append(photo)
			i += 1
		# solve the data
	return photos

def vertical_combinations(target_size,vertical_photos):
	
	combinations = []
	while(len(vertical_photos) > 1):
		tags = set()
		first_photo = vertical_photos.pop()
		tags.add(first_photo['tags'])
		for second_photo in vertical_photos:
			tags_temp = tags
			tags_temp.add(second_photo['tags'])
			if len(tags_temp) == target_size:
				combination.append((first_photo,second_photo))
				break


