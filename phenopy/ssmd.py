from numpy import mean, var, cov, sqrt

def ssmd(a, b):
	"""
	Computes a strictly standardised mean difference (ssmd)
	"""
	mu_a = mean(a)
	mu_b = mean(b)
	var_a = var(a)
	var_b = var(b)
	cov_ab = cov([a, b])

	beta = (mu_a - mu_b) / math.sqrt(var_a + var_b - 2 * cov_ab)

	return(beta)