import logging
import random

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
	photos = []

	while(len(vertical_photos) > 1):
		[a,b] = random.choices(list(range(len(vertical_photos) - 1)),k=2)
		combinations.append((vertical_photos[a],vertical_photos[b]))
		if a < b:
			del vertical_photos[b]
			del vertical_photos[a]
		else:
			del vertical_photos[a]
			del vertical_photos[b]

	for combination in combinations:
		photo = {}
		photo['id'] = (combination[0]['id'],combination[1]['id'])
		photo['tags'] = set(list(combination[0]['tags']) + list(combination[1]['tags']))
		photos.append(photo)

	return (photos, vertical_photos)


