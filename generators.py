# Generators
import time
import random

# 1. Built-in generator
def standard(n):
	'''
	Returns a Python integer with k random bits.
	This method is supplied with the MersenneTwister generator and some other generators may also provide it as an optional part of the API.
	It produces 53-bit precision floats and has a period of 2**19937-1.
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

	buffer = []

	for i in range(1, 8*n+1):
		x_t = init[17]^init[15]^init[11]^init[0] #produce bits
		init = shift_register(init, x_t)
		buffer.append(x_t)
		if i%8 == 0:
			x_byte = int(''.join([str(x) for x in buffer]), 2) # byte in decimal form
			seq.append(x_byte)
			del buffer[:] # clear buffer

	return seq

def L89(n):
	init = [random.getrandbits(1) for _ in range(89)]
	seq = []

	buffer = []

	for i in range(1, 8*n+1):
		x_t = init[51]^init[0]
		init = shift_register(init, x_t)
		buffer.append(x_t)
		if i%8 == 0:
			x_byte = int(''.join([str(x) for x in buffer]), 2) # byte in decimal form
			seq.append(x_byte)
			del buffer[:]

	return seq

def wolfram(n, r0=None):
	if r0 is None:
		r0 = int(time.time())
	seq = []

	buffer = []
	#print('r0:\t{:032b}'.format(r0))

	for i in range(1, 8*n+1):
		#print('r0<<1:\t{:032b}'.format(r0<<1))
		#print('r0>>1:\t{:032b}'.format(r0>>1))
		#print('r0|>>:\t{:032b}'.format(r0|(r0>>1)))
		r0 = (r0<<1)^(r0|(r0>>1))
		r0 = int('{:032b}'.format(r0)[-32:],2)
		#print('r0:\t{:032b}'.format(r0))
		#print('\n')
		x_i = '{:032b}'.format(r0)[-1]
		buffer.append(x_i)
		if i%8 == 0:
			x_byte = int(''.join([str(x) for x in buffer]), 2) # byte in decimal form
			seq.append(x_byte)
			del buffer[:]

	return seq
	
def librarian():
    with open('text_games.txt', 'r') as f:
        text = f.read()
    print(len(text))
    array_of_bytes = []
    for symb in text:
        if symb.isalpha():
            array_of_bytes.append(ord(symb))
    return array_of_bytes[:1000000]


def blum_mical(bits):
    start_time = time.time()
    p = int("CEA42B987C44FA642D80AD9F51F10457690DEF10C83D0BC1BCEE12FC3B6093E3", 16)
    a = int("5B88C41246790891C095E2878880342E88C79974303BD0400B090FE38A688356", 16)
    array_of_bytes = []
    t = random.randint(1, p - 1)
    if bits:
        p_divided = (p - 1) / 2
        for _ in range(1000000):
            one_byte = ''
            for _ in range(8):
                new_t = pow(a, t, p)
                if new_t < p_divided:
                    one_byte += '1'
                else:
                    one_byte += '0'
                t = new_t
            integer_byte = int(one_byte, 2)
            array_of_bytes.append(integer_byte)
    else:
        #p_divided = (p - 1)/256
        for _ in range(1000000):
            new_t = pow(a, t, p)
            t_divided = new_t * 256
            result = t_divided/(p-1)
            residue = t_divided%(p-1)
            if residue:
                k = result
            else:
                k = result-1
            array_of_bytes.append(k)
            t = new_t
    #print(array_of_bytes[:5])
    #print(len(array_of_bytes))
    print(time.time() - start_time)
    return array_of_bytes


def bbs_gen(bits):
    start_time = time.time()
    p = int("D5BBB96D30086EC484EBA3D7F9CAEB07", 16)
    q = int("425D2B9BFDB25B9CF6C416CC6E37B59C1F", 16)
    n = p * q
    r = random.randint(2, n)
    array_of_bytes = []
    for i in range(1000000):
        if bits:
            one_byte = ''
            for i in range(8):
                r = pow(r, 2, n)
                one_byte += str(pow(r, 1, 2))
            array_of_bytes.append(int(one_byte, 2))
        else:
            r = pow(r, 2, n)
            array_of_bytes.append(pow(r, 1, 256))
    #print(array_of_bytes[:10])
    print(time.time() - start_time)
    return array_of_bytes


def lfr_geffie(l1, l2, l3, array_1, array_2, array_3, number_to_generate):
    start_time = time.time()
    def lfr(l, array):
        l_temp = l[:]
        new_el = 0
        for numb in array:
            new_el ^= l_temp[numb]
        el = l_temp.pop()
        #print(new_el)
        l_temp.insert(0, new_el)
        return el, l_temp

    l1_arr = [int(i) for i in l1]
    l2_arr = [int(i) for i in l2]
    l3_arr = [int(i) for i in l3]
    array_of_bytes = []
    """array_of_i = numbers of not null coefficient of polynom
       number_to_generate = how many random number we need to generate"""
    for _ in range(number_to_generate):
        one_byte = ''
        for _ in range(8):
            l1_el, l1_arr = lfr(l1_arr, array_1)
            l2_el, l2_arr = lfr(l2_arr, array_2)
            l3_el, l3_arr = lfr(l3_arr, array_3)
            z_el = bool(l3_el & l1_el) ^ ((True ^ bool(l3_el)) & l2_el)
            one_byte+=str(z_el)
        array_of_bytes.append(int(one_byte,2))
    #print(array_of_bytes[:5])
    print(time.time()-start_time)
    return array_of_bytes

