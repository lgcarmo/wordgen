#!/usr/bin/python

import argparse
import sys
import random
from random import randrange
import itertools


parser = argparse.ArgumentParser(description='Requests.')
parser.add_argument('-w', dest='k_vetor', help='lista dado:dados:senhas', required=True)
parser.add_argument('-n', dest='k_rep', help='numero de repeat -n x', required=True)
parser.add_argument('-l', dest='k_low', help='lista com Lowercase -l lower (no required)', required=False)
parser.add_argument('-c', dest='k_num', help='randomiza numeros', required=False)




args = parser.parse_args()

n =(int(args.k_rep))

chrs =(args.k_vetor).split(':')


for xz in itertools.product(chrs, repeat=n):
	print('').join(xz)
	print(args.k_num)

	if args.k_low == 'lower':
		print('').join(xz).capitalize

	