import numpy as np
from string import uppercase
from itertools import product

def num_to_well(num, plate = 96L):

	def num_to_well_single(num, plate = 96L):
	
		"""
		Converts well numbers into alpha-numeric well IDs
		"""
	
		number = num -1 # removes 0 indexing issues
	
		if num > plate:
			return "Error: well number greater than wells in plate"
	
		if plate == 96:
			rows = uppercase[0:8]
			columns = range(1, 13)
	
		if plate == 384:
			rows = uppercase[0:16]
			columns = range(1, 25)
	
		# generate all possible wells in an array
		combinations = product(rows, columns)
		comb_array = np.array(list(combinations))
		out = str(comb_array[number,0]) + str(comb_array[number,1])
		return out

	new_list = []

	for i in num:
		tmp = num_to_well_single(i, plate)
		new_list.append(tmp)
	return new_list