#given a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#Write one line of Python that takes this list a 
#and makes a new list that has only the even elements of this list in it.

a = [2,11,13,24,33,60,46,57,36]

print([i for i in a if i%2 == 0])


#b = []
#for i in a:
#    if i % 2 == 0:
#        b.append(i)
#        print (b)
 