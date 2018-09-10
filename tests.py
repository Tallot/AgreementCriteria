# Testing different generators using defined criteria

from generators import *
from criteria import *

def test(generator, alpha=0.1):
	seq = generator()
	
	test1 = equiprobability_signs_criterion(seq, alpha=alpha)
	test2 = independency_signs_criterion(seq, alpha=alpha)
	test3 = uniformity_signs_criterion(seq, alpha=alpha)
	
	print('For alpha {}:'.format(alpha))
	print(test1,'\n', test2,'\n', test3,'\n')
	
	
if __name__=='__main__':
	generators = [standard] #will be added soon
	
	for generator in generators:
		test(generator, 0.1)
		test(generator, 0.05)
		test(generator, 0.01)