def namelist(names):
    namesList = []
    
    for dictionary in names:
        namesList.append(value)
    
    nString = ''
    
    for index in range(len(names)):
        if index == 0:
            nString = nString + names[index]
        elif index == len(names)-1:
            nString = nString + ' & ' + names[index]
        
    return nString

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print('returns Bart, Lisa & Maggie')

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
print('returns Bart & Lisa')

print(namelist([ {'name': 'Bart'} ]))
print('returns Bart')

print(namelist([]))
print("returns ''")