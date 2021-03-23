def square_or_square_root(arr):
    '''
    Input an array of integers, and this will return an array in which every value is the square root of the input's value,
    except if there is no integer square root, in which case the value is squared.
    '''   
    ret_arr = []                            #make a return array, then
    for val in arr:                         #for every value,
        if int(val**(1/2))<val**(1/2):      #if the value has no square root
            ret_arr.append(val**2)          #square it
        else:                               #otherwise,
            ret_arr.append(val**(1/2))      #square root it
    return ret_arr                          #finally, return the array