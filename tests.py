# Testing different generators using defined criteria

from generators import *
from criteria import *

def test(seq, alpha=0.1):

	test1 = equiprobability_signs_criterion(seq, alpha=alpha)
	test2 = independency_signs_criterion(seq, alpha=alpha)
	test3 = uniformity_signs_criterion(seq, alpha=alpha)

	print('For alpha {}:'.format(alpha))
	print(test1,'\n', test2,'\n', test3,'\n')


if __name__=='__main__':

	sequences = []

	standard_seq = standard(100000)
	sequences.append(standard_seq)
	print('Standard sequence created\n')


	lehmerlow_seq = lehmer_low(100000)
	sequences.append(lehmerlow_seq)
	print('LehmerLow sequence created\n')


	lehmerhigh_seq = lehmer_low(100000)
	sequences.append(lehmerhigh_seq)
	print('LehmerHigh sequence created\n')

	l_20_seq = L20(100000)
	sequences.append(l_20_seq)
	print('L20 sequence created\n')

	l_89_seq = L89(100000)
	sequences.append(l_89_seq)
	print('L89 sequence created\n')

	wolfram_seq = wolfram(100000)
	sequences.append(wolfram_seq)
	print('Wolfram sequence created\n')

	global_start = time.time()

	for seq in sequences:
		start = time.time()
		test(seq, 0.1)
		finish  = time.time() - start
		print('Test took {} seconds'.format(finish))
		#test(seq, 0.05)
		#test(seq, 0.01)

	global_finish  = time.time() - global_start
	print('Entire job took {} seconds'.format(global_finish))
