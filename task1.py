import itertools
 
if __name__ == '__main__':
    symbols = 'bac'
    string = list(symbols)
    permutations = list(itertools.permutations(string))
    print([''.join(permutation) for permutation in permutations])