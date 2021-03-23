# def maskify(cc):

#     revCC = list(cc[::-1])
#     index = 0
    
#     for char in revCC:
#         if index > 3:
#             revCC[index] = '#'
#         index += 1
    
#     revCC = ''.join(revCC[::-1])
    
#     return revCC

# # def maskify(cc):

# #     revCC = list(cc[::-1])
    
# #     for num in range(len(revCC)):
# #         if num > 3:
# #             revCC[num] = '#'
    
# #     revCC = ''.join(revCC[::-1])
    
# #     return revCC

# def maskify(cc):
    
#     newCC = ''                        # Set up return string

#     for num in range(len(cc)):        # For each character
#         if num < len(cc) - 4:         # If the character is not the last four
#             char = '#'                # Change it to '#'
#         else:                         # Otherwise
#             char = cc[num]            # Don't
#         newCC = newCC + char          # Then add it to the return string
    
#     return newCC

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]


print(maskify(''))
print(maskify('123'))
print(maskify('SF$SDfgsd2eA'))