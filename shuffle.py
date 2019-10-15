# -h : -h help
# -n counts : Uniform random counts

import numpy as np
import getopt
import sys
import random

def usage():
    print(' -h help \n' \
          ' -n counts \n')

# TODO : suffle & turn over cards for [counts] times
def shuffle(counts):
    # TODO : generate 1~100 cards
    cards = list(range(1,101))

    # TODO : suffle & turn over cards and calculate hit times
    n_list = []
    for i in range(0, counts) :
        random.shuffle(cards)
        sum = 0
        for index, item in enumerate(cards, 1):
            if index == item:
                sum += 1
        n_list.append(sum)
    
    print("expectation : %f" % np.mean(n_list))
    print("variance : %f" % np.var(n_list))


if __name__ == '__main__':  
    try:
        options, args = getopt.getopt(sys.argv[1:], "hn:",[])
        for name, value in options:
            if name in ('-h'):
                usage()
            elif name in ('-n'):
                shuffle(int(value))
    
    except getopt.GetoptError:
        usage()
