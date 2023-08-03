import argparse
import itertools


def leet_convert(text):
    leet_dict = {'a': '4', 'e': '3', 't': '7'}
    return ''.join(leet_dict.get(char.lower(), char) for char in text)

def generate_combinations(chrs, n):
    return itertools.product(chrs, repeat=n)

def capitalize_if_required(text, cap_type):
    if cap_type == 'upper':
        return text.capitalize()
    elif cap_type == 'upleet':
        return leet_convert(text).capitalize()
    else:
        return text

def main():
    parser = argparse.ArgumentParser(description='Requests.')
    parser.add_argument('-w', dest='k_vetor', help='lista dado:dados:senhas', required=True)
    parser.add_argument('-m', dest='k_min', help='minimum 0', default=0, required=False, type=int)
    parser.add_argument('-M', dest='k_max', help='Max X', default=2, required=False, type=int)
    parser.add_argument('-c', dest='k_cap', help='Module: upper | upleet', required=False)
    parser.add_argument('-l', '--leet', help='leet: a:4 e:3 t:7', dest='k_leet', action='store_true', required=False)
    parser.add_argument('-o', '--output', type=argparse.FileType(mode='w'), dest='k_output', help='Salva a wordlist em um arquivo.')
    args = parser.parse_args()

    n = args.k_min
    m = args.k_max

    chrs = args.k_vetor.split(':')

    while n <= m:
        for combination in generate_combinations(chrs, n):
            text = ''.join(combination)
            text = capitalize_if_required(text, args.k_cap)

            if args.k_leet:
                text = leet_convert(text)

            if args.k_output is not None:
                args.k_output.write(text + '\n')
            else:
                if not text.isnumeric():
                    print(text)

        n += 1

if __name__ == "__main__":
    main()
