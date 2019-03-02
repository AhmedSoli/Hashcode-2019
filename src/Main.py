import os
from Solver import * 
from Parser import * 
from multiprocessing import *

def compute(file):
	photos,tags = parse('../data/' + file)
	solver = Solver(photos,tags,file)
	slides = solver.solve_complex()
	generate_solution(slides,file)

# get all data files
files = os.listdir('../data')
# sort from smallest to biggest filfes
files.sort(key = lambda s: os.stat('../data/' + s).st_size)
# print sorted array for verification
print("Files {}".format(files))
# init pool
p = Pool(1)
# map compute function to pool
print(p.map(compute, files[0:-1]))
