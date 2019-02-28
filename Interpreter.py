from Grid import * 

# read file
files = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_big.in']

for file in files:
	print("Working on file {0}".format(file))
	with open('data/' + file,"r") as opened_file:
		# counter for lines
		i = 0
		for line in opened_file:
			if i == 0:
				configs = line.split(' ')
				# init new grid for storing the pizza
				grid = Grid(configs,file)
			else:
				# remove \n from end of line and split all cells
				cells = line.replace('\n','')
				# append cells to the grid and calculate important numbers
				grid.append(cells,i-1)
			i += 1
		grid.solve()