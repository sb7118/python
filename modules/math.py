'''
math module contains different types of mathematical functions.
 most of the functions in this module returns a float value
'''
import math
''' 
print(math.sqrt(169)) #returns squareroot of given number
print(math.pow(2,3)) #returns power of coefficient 'x' with power 'y'
print(math.ceil(4.1)) #returns by rounding up to nearest  lsrge integer
print(math.floor(4.1)) #returns by rounding up to the nearest small integer
print(math.sin(0)) #returns sine value
print(math.cos(0))  #returns cosine value
print(math.tan(45)) # returns tangent value
print(math.pi) #pi is a math constant
print(math.fabs(-2)) #it removes negative sign
print(math.isfinite(-1/12)) #checks weather the no. is finite or not
print(math.isinf(1/9)) #checks weather the no. is infinite or not
print(int(math.sqrt(3))) #int() removes the floating point numbers
'''


'''practice!'''
'''
WAP to calculate the area of a circle
'''

radius = int(input('enter radius : '))
area = math.pi*math.pow(radius,2)
print(area)
