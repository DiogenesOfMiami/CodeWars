def assert_equals(one, two):
    if one == two:
        print('Succeeded! \n')
    else:
        print('Failed:')
        print(one)
        print("Should equal")
        print(two)

def move_zeros(array):
    # returnA = array[:]
    # zeroCount = 0
    # while 0 in returnA:
    #     returnA.remove(0)
    #     zeroCount += 1

    # returnA = []
    # zeroCount = 0

    # for e in array:
    #     try:
    #         e + 1
    #         zeroCount += 1
    #     else:
    #         returnA.append(e)
            
    # while zeroCount > 0:
    #     returnA.append(0)
    #     zeroCount -= 1

    returnA = []
    zeroCount = 0

    for e in array:
        # try:
        #     if int(e) is 0:
        #         zeroCount += 1
        #     else:
        #         returnA.append(e)
        # except:
        #     returnA.append(e)
        if type(e) is int or type(e) is float:
            if int(e) is 0:
                zeroCount += 1
            else:
                returnA.append(e)
        else:
            returnA.append(e)


    while zeroCount > 0:
        returnA.append(0)
        zeroCount -= 1
    
    return returnA

assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])