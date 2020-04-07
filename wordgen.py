#!/usr/bin/python

import argparse
import sys
import random
from random import randrange
import itertools

parser=argparse.ArgumentParser (description='Requests.')
parser.add_argument ('-w', dest='k_vetor', help='lista dado:dados:senhas', required=True)
parser.add_argument ('-m', dest='k_min', help='minum 0', required=True)
parser.add_argument ('-M', dest='k_max', help='Max X', required=True)
parser.add_argument ('-c', dest='k_cap', help='Captalize', required=False)

args=parser.parse_args ()

n=(int (args.k_min))
m=(int (args.k_max))

chrs=(args.k_vetor).split (':')

while n <= m:
    n+=1
    for xz in itertools.product (chrs, repeat=n):
        print ('').join (xz)
    #	print(args.k_num)

    for xz in itertools.product (chrs, repeat=n):
        if args.k_cap == 'upper':
            print ('').join (xz).capitalize()
