#Take two lists and write a program that
#returns a list that contains only the elements that 
#are common between the lists (without duplicates)

import random

a = list(random.sample(range(1,30), 10))

b = list(random.sample(range(10,40), 14))

#result = [i for i in a if i in b]
result = list(set(a) & set(b))

print( "The first list is :", a )
print("The second list is :",b )
print("The common elements are :", result)