from Grid import * 
import os

# read file
files = os.listdir('data')

for file in files:
	print("Working on file {0}".format(file))
	with open('data/' + file,"r") as opened_file:
		# counter for lines
		i = 0
		for line in opened_file:
			photos = []
			if i == 0:
				number_of_photos = line.split(" ")[0]
				print(number_of_photos)
			else:
				photo = {}
				vals = line.split(' ')
				photo['direction'] = vals[0]
				vals[-1] = vals[-1].replace('\n','')
				photo['tags'] = vals[2:]
				print(photo)
				break
			i += 1