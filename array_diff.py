# It should remove all values from list a, which are present in list b.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

# def array_diff(a, b):
#     for e in a:
#         if e in b:
#             while e in a:
#                 a.remove(e)
#     for e in b:
#         if e in a:
#             while e in b:
#                 b.remove(e)
#     print(a+b)
#     return a+b

# def array_diff(a, b):
#     for e in a:
#         if e in b:
#             while e in a:
#                 a.remove(e)
#     print("Resulted", end=' ')
#     print(a)
#     return a

def array_diff(a, b):

    r = []

    for e in a:
        if e not in b:
            r.append(e)



    print("Resulted", end=' ')
    print(r)
    return r

array_diff([1,2,2,2,3],[2])
print("Expected [1, 3]")
array_diff([-7, -10, 7, -6, 11, -19, 15, 17],[4, -11, -17, -5, -17, -6, 20, -10, 13, 4, 18, -19, 9, -8, -11, 11, -18, -11, 4])
print("Expected [-7, 7, 15, 17]")