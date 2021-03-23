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
    print(rList)                    #REMOVE
    return rList

permutations("Our servers are configured to only allow a certain amount of time for your code to execute. In rare cases the server may be taking on too much work and simply wasn't able to run your code efficiently enough. Most of the time though this issue is caused by inefficient algorithms. If you see this error multiple times you should try to optimize your code further.")