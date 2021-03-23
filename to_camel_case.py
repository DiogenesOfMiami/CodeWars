# def to_camel_case(text):
#     try:
#         returnText = text[0]
#     except:
#         return ''
        
#     word = ''
#     index = 1
#     for letter in text[1:]:
#         if letter.isalpha():
#             if index < 1:
#                 word = word + letter.upper()
#             else:
#                 word = word + letter
#             index += 1
#         else:
#             returnText = returnText + word
#             word = ''
#             index = 0
#     print(returnText)                                     #DEBUG PRINT
#     return returnText

# def to_camel_case(text):
#     try:
#         word = text[0]
#     except:
#         return ''
#     index = 1
#     for letter in text[1:]:
#         if letter.isalpha():
#             if index < 1:
#                 word = word + letter.upper()
#             else:
#                 word = word + letter
#             index += 1
#         else:
#             index = 0
#     return word

# Someone else's:

# def to_camel_case(text):
#     cap = False
#     newText = ''
#     for t in text:
#         if t == '_' or t == '-':
#             cap = True
#         else:
#             if cap == True:
#                 t = t.upper()
#             newText = newText + t
#             cap = False
#     return newText

print(to_camel_case(''))
print(to_camel_case('the_stealth_warrior'))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))