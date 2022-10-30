"""a simple calculator"""
import math
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):     
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def power(a,b):
    return math.pow(a,b)

def sqrt(a):
    return math.sqrt(a)


def prime(a):
    count = 0
    for i in range(1,a+1):
        if a % i == 0:
            count += 1
    if count==2:
        return "prime"
    else:
        return "composite"

def factorial(a):
    factorial = 1
    for i in range(1,a+1):
        factorial = factorial * i 
    return factorial

print(''' features of this calculator:
      1= additoin , 2= substraction , 3= multiplication , 4= divison , 5= modulus-division , 6= power , 7= square-root,
      8= prime-checker 9= factorial
      ''')

choice = int(input("enter your choice number (1-9)"))
if choice == 1 or choice ==2 or choice == 3 or choice == 4 or choice ==5  or choice == 6:
    a = int(input('enter first number '))
    b = int(input('enter second number '))
    if choice == 1:
        print(add(a,b))
    elif choice == 2:
        print(sub(a,b))
    elif choice == 3:
        print(mul(a,b))
    elif choice == 4:
        print(div(a,b))
    elif choice ==5:
        print(mod(a,b))
    else:
        print(power(a,b))
else :
    a = int(input("enter any number "))
    if choice == 7:
        print(sqrt(a))
    elif choice ==8:
        print(prime(a))
    else :
        print(factorial(a))