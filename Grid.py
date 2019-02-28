import numpy as np

class Grid:

	def __init__(self,configs,file):
		num_of_rows = configs[0]
		num_of_cols = configs[1]
		# initialising the grid with zeros (0 => Mushroom, 1 => Tomato, -1 => used)
		self.cells = np.zeros((int(num_of_rows),int(num_of_cols)))
		# setting the minimum number required of each ingredient per slice
		self.min_ingredients = int(configs[2])
		# setting the max number of cells allowed in each slice
		self.max_cells = int(configs[3])
		# dict for storing mushrooms and tomatos
		self.ingredients = {'mushrooms': [],'tomatos': []}
		# set file name
		self.file = file

	def __str__(self):
		return "{0}".format(self.cells)

	def append(self, cells,row):
		for col, cell in enumerate(cells):
			if cell == "M":
				self.ingredients['mushrooms'].append((row,col))
				self.cells[row,col] = 0
			else:
				self.ingredients['tomatos'].append((row,col))
				self.cells[row,col] = 1

	def get_cell_neighbors(self,cell):
		neighbors = set()
		row = cell[0]
		col = cell[1]

		if row > 0:
			neighbors.add((row - 1,col))

		if row < len(self.cells) - 1:
			neighbors.add((row + 1,col))

		if col > 0:
			neighbors.add((row,col - 1))

		if col < len(self.cells[0]) - 1:
			neighbors.add((row,col + 1))

		return neighbors

	def get_slice_borders(self,slice):
		min_row = float("inf")
		min_col = float("inf")
		max_row = 0
		max_col = 0
		for (row,col) in slice[0] + slice[1]:
			min_row = min(min_row,row)
			max_row = max(max_row,row)
			min_col = min(min_col,col)
			max_col = max(max_col,col)

		borders = {'min_row': min_row, 'max_row': max_row, 'min_col': min_col, 'max_col': max_col}
		return borders

	def get_slice_center(self,borders):
		return (int((borders['min_row'] + (borders['max_row'] - borders['min_row']) / 2)),int((borders['min_col'] + (borders['max_col'] - borders['min_col']) / 2)))

	def find_min_slice(self,start):
		ingredient = self.cells[start]
		other_ingredient = 1 - ingredient
		
		visited, queue = set(), [start]
		found = {ingredient:[],other_ingredient:[]}

		while queue and len(found[ingredient]) < self.min_ingredients:
			cell = queue.pop(0)
			topping = self.cells[cell]
			if cell not in visited and topping != -1:
				if topping == ingredient:
					found[ingredient].append(cell)
					borders = self.get_slice_borders(found)
					center = self.get_slice_center(borders)
					queue = [center]
				visited.add(cell)
				queue.extend(self.get_cell_neighbors(cell) - visited)

		for row in range(borders['min_row'],borders['max_row']+1):
			for col in range(borders['min_col'],borders['max_col']+1):
				if self.cells[(row,col)] == other_ingredient:
					found[other_ingredient].append((row,col))

		while queue and len(found[other_ingredient]) < self.min_ingredients:
			cell = queue.pop(0)
			topping = self.cells[cell]
			if cell not in visited and topping != -1:
				if topping == other_ingredient:
					found[other_ingredient].append(cell)
					borders = self.get_slice_borders(found)
					center = self.get_slice_center(borders)
					queue = [center]
				visited.add(cell)
				queue.extend(self.get_cell_neighbors(cell) - visited)

		return found

	def validate(self,borders):
		cells = 0
		mushrooms = 0
		tomatos = 0
		for row in range(borders['min_row'],borders['max_row']+1):
			for col in range(borders['min_col'],borders['max_col']+1):
				if self.cells[(row,col)] == -1:
					return False
				elif self.cells[(row,col)] == 0:
					mushrooms += 1
				else:
					tomatos += 1
				cells += 1
		if cells > self.max_cells or mushrooms < self.min_ingredients or tomatos < self.min_ingredients:
			return False
		else:
			return True

	def solve(self):
		if len(self.ingredients['mushrooms']) < len(self.ingredients['tomatos']):
			min_ingredient = 'mushrooms'
		else:
			min_ingredient = 'tomatos'

		slices = []

		for ingredient in self.ingredients[min_ingredient]:
			if self.cells[ingredient] != -1:
				slice = self.find_min_slice(ingredient)
				borders = self.get_slice_borders(slice)

				if self.validate(borders):
					slices.append(borders)

					for row in range(borders['min_row'],borders['max_row']+1):
						for col in range(borders['min_col'],borders['max_col']+1):
							self.cells[(row,col)] = -1

		# prepare solution file
		with open('solutions/' + self.file,"w+") as opened_file:
			slices_count = len(slices)
			opened_file.write("{0} \n".format(slices_count))
			for borders in slices:
				opened_file.write("{0} {1} {2} {3} \n".format(borders['min_row'],borders['min_col'],borders['max_row'],borders['max_col']))


