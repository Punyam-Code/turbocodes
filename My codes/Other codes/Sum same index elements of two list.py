#Sum same index elements of two list and concatenate the rest 


#result=[6, 8, 10, 12, 14, 12, 13]
from itertools import zip_longest 
l1=[1,2,3,4,5]
l2=[5,6,7,8,9,12,13]
l3=[x+y for x,y in zip(l1,l2) ]+l1[len(l2):]+l2[len(l1):]   # Type 1
l4=[x+y for x,y in zip_longest(l1,l2,fillvalue=0)]          # Type 2
l5=list(map(sum,zip(l1,l2)))+l1[len(l2):]+l2[len(l1#):]     # Type 3
print(l5)
print(l3)
print(l4)