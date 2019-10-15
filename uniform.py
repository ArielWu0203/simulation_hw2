# -h : -h help
# -n counts : Uniform random counts

import numpy as np
import getopt
import sys
from numpy import mean

def usage():
    print(' -h help \n' \
          ' -n counts \n')

# TODO : Uniform random & calculate expctation
def uf_rdm(count):

    n_list = []

    # Uniform random
    for i in range(0, count):
        sum = 0
        n = 0
        while sum <=1 :
            sum += np.random.uniform(0,1)
            n += 1
        n_list.append(n)

    # calculate expctation
    print(mean(n_list))


if __name__ == '__main__':  
    try:
        options, args = getopt.getopt(sys.argv[1:], "hn:",[])
        for name, value in options:
            if name in ('-h'):
                usage()
            elif name in ('-n'):
                uf_rdm(int(value))
    
    except getopt.GetoptError:
        usage()
