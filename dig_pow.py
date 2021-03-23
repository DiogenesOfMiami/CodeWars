def dig_pow(n, p):
    powerSum = 0
    index = 0

    for digit in str(n):
        powerSum += int(digit)**(p+index)
        index += 1
    
    x = 1
    while x <= n:
        if n * x == powerSum:
            return x
        x += 1
       
    return -1

print(dig_pow(695, 2))