#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#Example: If you ask for a divisor of 15, your program should print, 1

num = int(input("Enter any Number: "))
list = []

for i in range(1,num+1):
    if num % i == 0:
        list.append(i)

        print(list)