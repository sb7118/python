'''WAP to reverse the input number by the user'''

num = int(input("enter any number : "))
remainder = 0
reverse = 0

while(num!= 0):
    remainder = num % 10
    reverse = (reverse*10) + remainder
    num = num / 10

print(reverse)