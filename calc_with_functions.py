# import sys

def zero(): 
    return 0
def one(): #your code here
    return 1
def two(): #your code here
    return 2
def three(): #your code here
    return 3
def four(): #your code here
    return 4
def five(): #your code here
    return 5
def six(): #your code here
    return 6
def seven(operator=''): #your code here
    # if len(sys.argv)<2:
    #     return 7
    # else:
    if operator == '':
        return 7
    # else:
        operator(7)
        
def eight(): #your code here
    return 8
def nine(): #your code here
    return 9

# def plus(): #your code here
# def minus(): #your code here
def times(): #your code here
# def divided_by(): #your code here




seven(times(five())) # must return 35
print("35 Expected")
four(plus(nine())) # must return 13
print("^ Should be 13")
eight(minus(three())) # must return 5
print("^ Should be 5")
six(divided_by(two())) # must return 3
print("^ Should be 3")