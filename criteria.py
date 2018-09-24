# Pearson's chi-squared criteria

import math
from collections import Counter
import numpy as np


quantiles = {0.99:2.326, 0.95:1.645, 0.9:1.282}
l=255

def equiprobability_signs_criterion(seq:'bytes in decimal form', alpha=0.1):
	# Our hypothesis H0 is that all bytes in sequence have equal probability

	chi_squared = 0
	n = len(seq)/256
	counts = Counter(x for x in seq)# super efficient
	for byte in range(256):
		nu = counts[byte]
		chi_squared += ((nu-n)**2 / n)

	chi_squared_one_minus_alpha = math.sqrt(2*l)*quantiles[1-alpha]+l

	if chi_squared <= chi_squared_one_minus_alpha:
		return (True, chi_squared, chi_squared_one_minus_alpha)
	else:
		return (False, chi_squared, chi_squared_one_minus_alpha)

def independency_signs_criterion(seq:'bytes in decimal form', alpha=0.1):
	n = len(seq)//2

	# Our hypothesis H0 is that all bytes in sequence are independent of previous ones

	couples = [(seq[2*i],seq[2*i+1]) for i in range(n)]

	chi_squared = 0

	alphas_j = Counter(x[1] for x in couples)
	nus_i = Counter(x[0] for x in couples)
	
	couples = np.asarray(couples, dtype='i4,i4')
	unique, counts = np.unique(couples, return_counts=True)# super efficient

	for i in range(256):
		nu_i = nus_i[i]

		for j in range(256):
			alpha_j = alphas_j[j]
			
			aim = np.asarray([(i,j)], dtype='i4,i4')
			nu_i_j = counts[np.where(unique == aim)]

			if nu_i > 0 and alpha_j > 0 and len(nu_i_j) > 0:
				chi_squared += nu_i_j[0]**2/(nu_i*alpha_j)

	chi_squared = n*(chi_squared-1)

	chi_squared_one_minus_alpha = math.sqrt(2*l**2)*quantiles[1-alpha]+l**2

	if chi_squared <= chi_squared_one_minus_alpha:
		return (True, chi_squared, chi_squared_one_minus_alpha)
	else:
		return (False, chi_squared, chi_squared_one_minus_alpha)

def uniformity_signs_criterion(seq:'bytes in decimal form', r=0, alpha=0.1):
	if r == 0:
		r = 1 + int(math.log(len(seq))/math.log(2))
	m = len(seq)//r
	n = m*r
	seq = seq[:n]
	# Our hypothesis H0 is that all bytes in sequence are uniformly distributed
	chi_squared = 0
	
	counts = Counter(x for x in seq)

	for i in range(256):
		nu_i = counts[i]
		for j in range(r):
			nu_i_j = seq[j*m:j*m+m].count(i)

			if nu_i > 0:
				chi_squared += nu_i_j**2/(nu_i*m)

	chi_squared = n*(chi_squared-1)

	chi_squared_one_minus_alpha = math.sqrt(2*l*(r-1))*quantiles[1-alpha]+l*(r-1)

	if chi_squared <= chi_squared_one_minus_alpha:
		return (True, chi_squared, chi_squared_one_minus_alpha)
	else:
		return (False, chi_squared, chi_squared_one_minus_alpha)