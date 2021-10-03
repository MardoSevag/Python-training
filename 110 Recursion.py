import sys
import math
import random
import re

max = 20
permutations = list()
rand_list = 0
cnt = 1

def generate_permutations(a, n):
    global cnt
    global rand_list

    if n==0:
        if cnt in rand_list:
            print(''.join(a))
        cnt += 1
    else:
        for i in range(n):
            generate_permutations(a, n-1)
            j = 0 if n%2 == 0 else i
            a[j], a[n] = a[n],a[j]
        generate_permutations(a, n-1)

if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

if not (5 <= len(sys.argv[1]) <= max):
    sys.stderr.write('A word should be between 5 and {} charecters long\n'.format(max))
    sys.exit(1)

word = sys.argv[1]
rand_list = random.sample( range( 1, math.factorial( len( word ) ) ), max )

generate_permutations(list(word), len(word)-1)