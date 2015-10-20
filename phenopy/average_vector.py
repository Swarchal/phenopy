import numpy as np

def average_vector(x):
	"""
	Calculates an average vector.
	Expected x as a 2D array with columns as elements
	and a row per vector
	"""

	mean_vector = x.mean(axis = 0)
	return(mean_vector) 