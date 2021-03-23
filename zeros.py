def zeros(n):
    
    fact = 1
    
    for i in range(1,n+1): 
        fact = fact * i 
    
    zeroes = 0
    
    for d in str(fact):
        if int(d) == 0:
            zeroes += 1
        else:
            zeroes = 0
             
    
    
    return zeroes

print(zeros(0), 0, "Testing with n = 0")
print(zeros(6), 1, "Testing with n = 6")
print(zeros(30), 7, "Testing with n = 30")
