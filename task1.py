def permutations(left, candidate=''):
 
    if len(left) == 0:
        print(candidate)
 
    for i in range(len(left)):
 
        newCandidate = candidate + left[i]
        newLeft = left[0:i] + left[i+1:]
 
        permutations(newLeft, newCandidate)
 
if __name__ == '__main__':

    string = 'bac'
    permutations(string)