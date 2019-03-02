import os
from Solver import * 
from Parser import * 
from multiprocessing import *

def compute(file):
	photos,tags = parse('../data/' + file)
	solver = Solver(photos,tags,file)
	slides = solver.solve_complex()
	generate_solution(slides,file)

files = os.listdir('../data')
p = Pool(1)
print(p.map(compute, files))
