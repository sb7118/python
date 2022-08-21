import numpy as np

intarr = np.array([(1,2,3,4,5 ),(6,7,8,9,10)])

print(intarr)
print(intarr.ndim) #shows the dimension of array
print(intarr.itemsize) #shows the size of array (in bytes)
print(intarr.dtype) #shows the datatypes of items
print(intarr.size) #shows the no. of items
print(intarr.shape) #shows the no. of rows and columns
print(intarr.reshape(5,2)) #reshapes the dimension of an array
print(intarr[0:,4]) #slices the part and returns single integer/float ':' selects all items
print(np.arange(20))#creates an array starting from 0 to given parameters (n-1)

#array split in numpy
newarr = np.array_split(intarr,2) #(<array name> , no. of pieces to split
print(newarr)
'''
filter in numpy
if the boolean index is True , it returns the item and if its false it doesn't returns
'''


newArr = np.array([3,6,9,12,15,18,21])
filterarr = [True ,False ,True ,False ,True,False, True]

print(newArr[filterarr])
#creates an empty array

filterArr = []

for x in newArr:
    if x < 15:
        filterArr.append(True)
    else:
        filterArr.append(False)

print(newArr[filterArr])
print(filterArr)

''' hstack = horizontal (column)
    vstack = vertical (row)
 '''
matrix = np.array([]) #empty array
matrix = np.hstack((matrix , np.array([1,2,3])))
matrix = np.vstack((matrix , np.array([4,5,6])))
print(matrix)
