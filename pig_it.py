# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


# def pig_it(text):
#     rText = ''
#     word = ''
#     firstL = ''
#     place = 0
#     for char in text:
#         if place == 0:
#             firstL = char
#             place += 1
#         elif char == ' ':
#             place = 0
#             word = word+firstL+'ay'+char
#             rText = rText+word
#             word = ''
#         else:
#             word = word+char
#             place += 1
#     return rText

# def pig_it(text):
#     wList = text.split()
#     rText = ''

#     for word in wList:
#         firstL = ''
#         place = 0
#         nWord = ''
#         special = False
#         for char in word:
#             if not char.isalpha():
#                 rText = rText+char
#                 special = True
#                 break
#             elif place == 0:
#                 firstL = char
#                 place += 1
#             else:
#                 nWord = nWord+char
#                 place += 1
#         if not special:
#             word = nWord+firstL+'ay'
#             rText = rText+word+' '
    
#     return rText


'''
Working versions below:
'''


# def pig_it(text):
#     wList = text.split()

#     for word in wList:
#         if word.isalpha():
#                 wList[wList.index(word)] = word[1:]+word[0]+'ay'

#     return ' '.join(wList)

def pig_it(text):
    wList = text.split()

    for word in wList:
        if word.isalpha():
                wList[wList.index(word)] = word[1:]+word[0]+'ay'

    return ' '.join(wList)



print(pig_it('Hello world !'))
print('elloHay orldWay !')