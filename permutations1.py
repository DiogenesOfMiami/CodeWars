def permutations(string):
    import math
    import random
    rList = []
    sList = list(string)

    # letterCount = {}
    # uniqL = len(set(string))

    while len(rList) < (math.factorial(len(string)))/(2*(len(string)-len(set(string)))):
    #while length of return is smaller than expected length of return calculated by factorial divided by two times the amount of unique characters
        random.shuffle(sList)
        s = ''.join(sList)
        if s not in rList:
            print('Adding ' + s + ' to return')        #REMOVE debug print
            rList.append(s)
        else:
            print('Ignoring duplicate ' + s)   
    




    print(rList)             #REMOVE
    return rList

permutations('aba')