import os
from Solver import * 
from Parser import * 

files = os.listdir('data')

for file in files:
    photos,tags = parse('data/' + file)
    for photo in photos:
    	print(photos[photo])
    	break
    slides = solve(photos,tags)
    
    generate_solution(slides,file)