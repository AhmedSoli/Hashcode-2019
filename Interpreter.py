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
		tags = list()
		first_photo = vertical_photos.pop()
		tags.extend(first_photo['tags'])
		for key,second_photo in enumerate(vertical_photos):
			if key == 1000:
				break
			tags_temp = tags
			tags_temp.extend(second_photo['tags'])
			if len(set(tags_temp)) <= target_size + 3 and len(set(tags_temp)) >= target_size - 3:
				combinations.append((first_photo,second_photo))
				break
	return (combinations, vertical_photos)

