def permutations(string):
    import math
    import random
    rList = []
    s = string[:]

    # letterCount = {}
    # uniqL = len(set(string))


    while len(rList) < (math.factorial(len(string)))/(2*(len(string)-len(set(string)))):
    #while length of return is smaller than expected length of return calculated by factorial divided by two times the amount of unique characters
        random.shuffle(s)
        if s not in rList:
            rList.append(s)   
    




    print(rList)             #REMOVE
    return rList

permutations('abab')