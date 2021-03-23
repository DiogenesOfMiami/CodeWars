# def alphabet_position(text):
#     returnS = ''
#     ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     index = 0
#     for char in text:
#         if char in ascii_letters:
#             if index > 0:
#                 returnS += ' '
#             index += 1
#             if ascii_letters.index(char) > 25:
#                 returnS += str(ascii_letters.index(char)-25)
#             else:
#                 returnS += str(ascii_letters.index(char)+1)
#     return returnS

def alphabet_position(text):
    returnS = ''
    for c in text.lower():
        if c.isalpha():
            returnS += ' '.join(str(ord(c)-96))
    return returnS

print(alphabet_position('banana'))