#!/usr/bin/python

import argparse
import sys
import random
from random import randrange
import itertools
from pyleet import Leet

################################
#K40S
#lgcarmo@protonmail.com
################################

parser=argparse.ArgumentParser (description='Requests.')
parser.add_argument ('-w', dest='k_vetor', help='lista dado:dados:senhas', required=True)
parser.add_argument ('-m', dest='k_min', help='minum 0', default=0, required=False)
parser.add_argument ('-M', dest='k_max', help='Max X', default=2, required=False)
parser.add_argument ('-c', dest='k_cap', help='Captalize', required=False)
parser.add_argument ('-l', '--leet', help='parameter -l leet', dest='k_leet', action='store_true', required=False)
parser.add_argument ('-o', '--output', type=argparse.FileType(mode='w'), dest='k_output', help='Salva a wordlist em um arquivo.')

args=parser.parse_args ()

n=(int (args.k_min))
m=(int (args.k_max))

chrs=(args.k_vetor).split (':')

while n <= m:
    n+=1
    for xz in itertools.product (chrs, repeat=n):
        if args.k_output is not None:
            list= ('').join (xz)
            args.k_output.write(list + '\n')
        else:
            print ('').join(xz)

    for xz in itertools.product (chrs, repeat=n):
        if args.k_cap == 'upper':
            if args.k_output is not None:
                upperlist=('').join (xz).capitalize()
                args.k_output.write(upperlist + '\n')
            else:

                print('').join (xz).capitalize()

    for xz in itertools.product (chrs, repeat=n):
        if args.k_leet:
            if args.k_output is not None:
                leet=('').join (xz)
                t=Leet (leet)
                tra = []
                tra.append(t.translate())
                for trans in tra:
                    args.k_output.write(trans + '\n')

            else:
                leet=('').join (xz)
                t=Leet (leet)
                print(t.translate())


