from numpy import mean, std, array

def z_score(x):
	mu = mean(x, None)
	sigma = std(x)
	return (array(x) - mu) / sigma