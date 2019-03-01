import os
from Solver import * 
from Parser import * 
from multiprocessing import Pool

def compute(file):
	photos,tags = parse('data/' + file)
	slides = solve_alt(photos,tags)
	generate_solution(slides,file)

files = os.listdir('data')
p = Pool(len(files))
print(p.map(compute, files))
