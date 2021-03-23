def permutations(string):
    import math
    import random
    rList = []
    sList = list(string)

    if len(string) == len(set(string)):
        expectedLength = math.factorial(len(string))
    else:
        expectedLength = (math.factorial(len(string)))/(2*(len(string)-len(set(string))))

    while len(rList) < expectedLength:    
        random.shuffle(sList)
        s = ''.join(sList)
        if s not in rList:
            rList.append(s)
            # print(rList)            #REMOVE
    print("Done", end=': ')
    print(rList)
    return rList

permutations("Chees")