def myfunc(n):
    return lambda a : a + n

mydoubler = myfunc(3)
mytripler = myfunc(4)

print(mydoubler(12))
print(mytripler(12))