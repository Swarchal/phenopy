from numpy import dot

def norm_vector(x):
	"""
	computes the length (norm) of a vector x
	"""
	norm_vector_out = math.sqrt(dot(x, x))
	return(norm_vector_out)