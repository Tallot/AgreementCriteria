# Generators
import time
import random

# 1. Built-in generator
def standard(n):
	'''
	Returns a Python integer with k random bits. This method is supplied with the MersenneTwister generator and some other generators may also provide it as an optional part of the API. It produces 53-bit precision floats and has a period of 2**19937-1.
	'''
	seq = [random.getrandbits(8) for _ in range(n)]
	return seq
	
def lehmer_low(n, x0=None):
	if x0 is None:
		x0 = int(time.time()) # random initialization
	m = 2**32
	a = 2**16+1
	c = 119
	x_prev = x0
	seq = []
	for i in range(n):
		x_next = pow(a*x_prev+c, 1, m)
		x_prev = x_next
		x_next = '{:032b}'.format(x_next)[-8:] # get 8 lowest bits
		seq.append(int(x_next,2)) # append value in decimal form
		
	return seq
	
def lehmer_high(n, x0=None):
	if x0 is None:
		x0 = int(time.time()) # random initialization
	m = 2**32
	a = 2**16+1
	c = 119
	x_prev = x0
	seq = []
	for i in range(n):
		x_next = pow(a*x_prev+c, 1, m)
		x_prev = x_next
		x_next = '{:032b}'.format(x_next)[:8] # get 8 lowest bits
		seq.append(int(x_next,2)) # append value in decimal form
		
	return seq
	
def shift_register(array, x):
	array = array[1:]
	array.append(x)
	return array
	
def L20(n):
	init = [random.getrandbits(1) for _ in range(19)]
	seq = []
	
	for i in range(n):
		x_t = init[17]^init[15]^init[11]^init[0]
		init = shift_register(init, x_t)
		seq.append(x_t)
		
	return seq
		
def L89(n):
	init = [random.getrandbits(1) for _ in range(89)]
	seq = []
	
	for i in range(n):
		x_t = init[51]^init[0]
		init = shift_register(init, x_t)
		seq.append(x_t)
		
	return seq

def wolfram(n):
	
	r0 = int(time.time())
	seq = []
	x0 = '{:032b}'.format(r0)[-1]
	seq.append(x0)
	
	for i in range(n):
		r0 = (r0<<1)^(r0|(r0>>1))
		x_i = '{:032b}'.format(r0)[-1]
		seq.append(x_i)
	
	return seq
	
	
	
	
	