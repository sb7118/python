""" WAP to find if the input number is perfect square or not """
import math 

num = int(input('enter any number : '))
sqr_num = math.sqrt(num) #squareroot of a number
absolute_num =int(sqr_num) #int removes floating point numbers

if absolute_num == sqr_num:
    print('perfect square')
else:
    print('not a perfect square')