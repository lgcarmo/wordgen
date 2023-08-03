import argparse
import itertools


def leet_convert(text):
    leet_dict = {'a': '4', 'e': '3', 't': '7'}
    return ''.join(leet_dict.get(char.lower(), char) for char in text)

parser = argparse.ArgumentParser(description='Requests.')
parser.add_argument('-w', dest='k_vetor', help='lista dado:dados:senhas', required=True)
parser.add_argument('-m', dest='k_min', help='minum 0', default=0, required=False)
parser.add_argument('-M', dest='k_max', help='Max X', default=2, required=False)
parser.add_argument('-c', dest='k_cap', help='Module: upper | upleet', required=False)
parser.add_argument('-l', '--leet', help='leet: a:4 e:3 t:7', dest='k_leet', action='store_true', required=False)
parser.add_argument('-o', '--output', type=argparse.FileType(mode='w'), dest='k_output', help='Salva a wordlist em um arquivo.')

args = parser.parse_args()

n = int(args.k_min)
m = int(args.k_max)

chrs = args.k_vetor.split(':')

while n <= m:
    n += 1
    for xz in itertools.product(chrs, repeat=n):
        if args.k_output is not None:
            lst = ''.join(xz)
            args.k_output.write(lst + '\n')
        else:
            s = u"%s" % ''.join(xz)
            if s.isnumeric():
                pass
            else:
                print(s)

    for xz in itertools.product(chrs, repeat=n):
        if args.k_cap == 'upper':
            if args.k_output is not None:
                upperlist = ''.join(xz).capitalize()
                args.k_output.write(upperlist + '\n')
            else:
                s = u"%s" % ''.join(xz).capitalize()
                if s.isnumeric():
                    pass
                else:
                    print(s)
        elif args.k_cap == 'upleet':
            upperlist = ''.join(xz).capitalize()
            s = u"%s" % leet_convert(upperlist)
            if s.isnumeric():
                pass
            else:
                print(s)

    for xz in itertools.product(chrs, repeat=n):
        if args.k_leet:
            if args.k_output is not None:
                leet = ''.join(xz)
                s = u"%s" % leet_convert(leet)
                if s.isnumeric():
                    pass
                else:
                    args.k_output.write(s + '\n')
            else:
                leet = ''.join(xz)
                s = u"%s" % leet_convert(leet)
                if s.isnumeric():
                    pass
                else:
                    print(s)
