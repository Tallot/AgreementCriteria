# Testing different generators using defined criteria

from generators import *
from criteria import *
from multiprocessing import Pool
from pprint import pprint

def test(seq, alpha=0.1):

    test1 = equiprobability_signs_criterion(seq, alpha=alpha)

    test2 = independency_signs_criterion(seq, alpha=alpha)

    test3 = uniformity_signs_criterion(seq, alpha=alpha)

    return (test1, test2, test3)


if __name__=='__main__':

    print('Generating sequences .... \n')

    sequences = []
    n=10**5

    standard_seq = standard(n)
    sequences.append(standard_seq)

    lehmerlow_seq = lehmer_low(n)
    sequences.append(lehmerlow_seq)

    lehmerhigh_seq = lehmer_high(n)
    sequences.append(lehmerhigh_seq)

    l_20_seq = L20(n)
    sequences.append(l_20_seq)

    l_89_seq = L89(n)
    sequences.append(l_89_seq)

    wolfram_seq = wolfram(n)
    sequences.append(wolfram_seq)

    print('All generators have created their sequences\n')
    print('Launching tests .........\n\n')

    global_start = time.time()

    pool = Pool(processes=3)
    results = pool.map(test, sequences)

    global_finish  = time.time() - global_start

    pool.close()
    pool.join()

    pprint(results)

    print('Entire job took {} seconds'.format(global_finish))
