def xo(s):
    
    xCount = 0
    oCount = 0
    
    for letter in s:
        if letter == 'x' or letter == 'X':
            xCount += 1
        elif letter == 'o' or letter == 'O':
            oCount += 1
            
    return xCount == oCount

print(xo('xo'))
print(xo('xo0'))
print(xo('xxxoo'))