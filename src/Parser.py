from pprint import *

def get_tag_ids(tag_ids,tags):
	ids = set()

	for tag in tags:
		if tag in tag_ids:
			ids.add(tag_ids[tag])
		else:
			tag_ids['last_id'] += 1
			tag_ids[tag] = tag_ids['last_id']
			ids.add(tag_ids['last_id'])

	return tag_ids,ids

def parse(file: str):
	print("Working on {}".format(file))
	with open(file, 'r') as opened_file:
		i = 0
		photos = {}
		tags = {}
		tag_ids = {'last_id':-1}
		for line in opened_file:
			if i == 0:
				number_of_photos = line.split(" ")[0]
				print(number_of_photos)
			else:
				photo = {}
				vals = line.split(' ')
				vals[-1] = vals[-1].replace("\n","")

				photo['orient'] = vals[0]
				photo['tags'] = int(vals[1])
				photo['id'] = i - 1
				tag_ids, photo['tag_ids'] = get_tag_ids(tag_ids,vals[2:]) 
				# photo['tag_ids'] = set(vals[2:])
				if photo['tags'] not in photos:
					photos[photo['tags']] = {'H':[],'V':[]}

				photos[photo['tags']][photo['orient']].append(photo)
				tags[photo['tags']] = tags.get(photo['tags'],{'H':0,'V':0})
				tags[photo['tags']][photo['orient']] += 1

			i += 1
	print("Done reading {} photos from {}".format(i-1,file))
	pprint("Tags {}".format(tags))
	return photos,tags

def generate_solution(slides,file):
	with open("../solution/" + file,"w+") as sol:
		sol.write("{}\n".format(len(slides)))
		for slide in slides:
			if isinstance(slide.id,int):
				sol.write("{}\n".format(slide.id))
			else:
				sol.write("{} {}\n".format(slide.id[0],slide.id[1]))
