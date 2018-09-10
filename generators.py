# Generators

# 1. Built-in generator
def standard():
	import random
	seq = [random.getrandbits(8) for _ in range(10000)]
	return seq