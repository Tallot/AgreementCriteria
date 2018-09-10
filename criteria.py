# Pearson's chi-squared criteria

import math

quantiles = {0.99:2.326, 0.95:1.645, 0.9:1.282}
l=255

def equiprobability_signs_criterion(seq:'bytes', alpha=0.1):
	# Our hypothesis H0 is that all bytes in sequence have equal probability
	
	chi_squared = 0
	n = len(seq)/256
	for byte in range(256):
		nu = seq.count(byte)
		chi_squared += ((nu-n)**2 / n)
		
	chi_squared_one_minus_alpha = math.sqrt(2*l)*quantiles[1-alpha]+l
		
	if chi_squared <= chi_squared_one_minus_alpha:
		return True
	else:
		return False
		
def independency_signs_criterion(seq:'bytes', alpha=0.1):
	n = len(seq)//2
	
	# Our hypothesis H0 is that all bytes in sequence are independent of previous ones
	
	couples = [(seq[2*i],seq[2*i+1]) for i in range(n)]
	
	chi_squared = 0
	
	alphas_j = []
	for j in range(256):
		alpha_j = sum([couples.count((l,j)) for l in range(256)])
		alphas_j.append(alpha_j)
	
	for i in range(256):
		nus_i = [couples.count((i,k)) for k in range(256)]
		nu_i = sum(nus_i)
		
		for j in range(256):
			nu_i_j = nus_i[j]
			 
			alpha_j = alphas_j[j]
			 
			chi_squared += nu_i_j**2/(nu_i*alpha_j)
	
	chi_squared = n*(chi_squared-1)
	
	chi_squared_one_minus_alpha = math.sqrt(2*l**2)*quantiles[1-alpha]+l**2
	
	if chi_squared <= chi_squared_one_minus_alpha:
		return True
	else:
		return False
		
def uniformity_signs_criterion(seq:'bytes', r=100, alpha=0.1):
	m = len(seq)//r
	n = m*r
	# Our hypothesis H0 is that all bytes in are uniformly distributed
	chi_squared = 0

	for i in range(256):
		nu_i = seq.count(i)
		for j in range(r):
			nu_i_j = seq[j*r:j*r+r].count(i)
			
			chi_squared += nu_i_j**2/(nu_i*m)
			
	chi_squared = n*(chi_squared-1)
			
	chi_squared_one_minus_alpha = math.sqrt(2*l*(r-1))*quantiles[1-alpha]+l*(r-1)

	if chi_squared <= chi_squared_one_minus_alpha:
		return True
	else:
		return False
			
			