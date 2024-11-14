# mylist = [22,20,35,5,7,9,11,3,125]

#for element in mylist:
 #   if element < 5:
       
  #      print(element)

#create a list first
list = [1,2,2,4,6,1,11,90,45,23,22,3,3,25]

for value in list:
    if value < 5:
        print (value)

#create  a new list
list1 = [value for value in list if value < 5]
print (list1)

#get user input
num = int(input("Type a number: "))

#check if the number is in the list
if num in list:
    print ("The number is in the List")
else:
    print ("The number is not in the list")
