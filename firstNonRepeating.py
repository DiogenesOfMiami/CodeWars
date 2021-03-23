# def first_non_repeating_letter(string):
#     dic = {}
#     for char in string:
#         if char.lower() in dic:
#             dic[char.lower()] += 1
#         else:
#             dic[char.lower()] = 1
#     for char in string:
#         if dic[char.lower()] == 1:
#             return char
#     return ''

def first_non_repeating_letter(string):
    for letter in string:
        if string.count(letter.lower()) == 1:
            return letter
            
    return ""

print(first_non_repeating_letter('a'), 'a')
print(first_non_repeating_letter('stress'), 't')
print(first_non_repeating_letter('moonmen'), 'e')

print('It should handle empty strings:')
print(first_non_repeating_letter(''), '')

print('It should handle all repeating strings:') 
print(first_non_repeating_letter('abba'), '')
print(first_non_repeating_letter('aa'), '')

print('It should handle odd characters:')
print(first_non_repeating_letter('~><#~><'), '#')
print(first_non_repeating_letter('hello world, eh?'), 'w')

print('It should handle letter cases:')
print(first_non_repeating_letter('sTreSS'), 'T')
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')