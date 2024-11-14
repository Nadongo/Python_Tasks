#Code that show the string is a Palindrome

string1 = input("Enter a string to check for palindrome: ")
string2 = string1[::-1]

print("These is the reverse:" + string2 )

if (string2 == string1):
    print("String is palindrome")
else:
    print("String is not a palindrome")