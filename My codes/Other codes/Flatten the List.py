#Flatten the List

#List [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#Flat List [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = []
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)

lis =  [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]
print('List', lis)
reemovNestings(lis)
print('Flat List', output)
