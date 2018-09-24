# coding: utf-8

# Testing different generators using defined criteria
from generators import *
from criteria import *

def test(seq, alpha=0.1):

	print('Current alpha in tests: {}'.format(alpha))

	print('Equiprobability test in progress ...')
	test1 = equiprobability_signs_criterion(seq, alpha=alpha)
	print('\t Test passing: {}\t Chi value: {}\t Chi theoretical: {}'.format(test1[0], test1[1], test1[2]))

	print('Independency test in progress ...')
	test2 = independency_signs_criterion(seq, alpha=alpha)
	print('\t Test passing: {}\t Chi value: {}\t Chi theoretical: {}'.format(test2[0], test2[1], test2[2]))

	print('Uniformity test in progress ...')
	test3 = uniformity_signs_criterion(seq, alpha=alpha)
	print('\t Test passing: {}\t Chi value: {}\t Chi theoretical: {}'.format(test3[0], test3[1], test3[2]))


if __name__=='__main__':

	print('Generating sequences .... \n')

	sequences = {}
	n=10**5

	standard_seq = standard(n)
	sequences['Built-in'] = standard_seq

	lehmerlow_seq = lehmer_low(n)
	sequences['LehmerLow'] = lehmerlow_seq

	lehmerhigh_seq = lehmer_high(n)
	sequences['LehmerHigh'] = lehmerhigh_seq

	l_20_seq = L20(n)
	sequences['L20'] = l_20_seq

	l_89_seq = L89(n)
	sequences['L89'] = l_89_seq

	wolfram_seq = wolfram(n)
	sequences['Wolfram'] = wolfram_seq
	
	geffe_seq = lfr_geffie('01010011001', '010001001', '0010010101', [10, 8], [8, 7, 5, 4], [9, 6], n)
	sequences['GeffeGenerator'] = geffe_seq
	
	bbs_byte_seq = bbs_gen(False) #BBS bytes version
	sequences['BBS-byte'] = bbs_byte_seq
	
	bbs_bit_seq = bbs_gen(True) #BBS bits version
	sequences['BBS-bit'] = bbs_bit_seq
	
	blum_mical_byte_seq = blum_mical(False) #BLUM-MICAL bytes version
	sequences['BlumMical-byte'] = blum_mical_byte_seq
	
	blum_mical_bit_seq = blum_mical(True) #BLUM-MICAL bits version
	sequences['BlumMical-bit'] = blum_mical_bit_seq
	
	librarian_seq = librarian() #LIBRARIAN VERSION
	sequences['Librarian'] = librarian_seq
	
	print('All generators have created their sequences\n')
	print('Launching tests .........\n\n')

	global_start = time.time()

	for (gen, seq) in sequences.items():
		print('Testing {} generator!\n'.format(gen))
		start = time.time()
		test(seq, 0.1)
		finish  = time.time() - start
		print('Test took {} seconds\n\n'.format(finish))

	global_finish  = time.time() - global_start
	print('Entire job took {} seconds'.format(global_finish))
