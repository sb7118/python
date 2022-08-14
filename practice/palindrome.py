'''this is palindrome checking program'''

name = input("enter your name : ")
i = len(name)-1
string = ""

while(i!=-1):
    string += name[i]
    i-= 1

if string == name:
    print("palindrome")
else:
    print("not palindrome")


