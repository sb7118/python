'''n = 5
for i in range(n):
    for j in range(n+1):
        print('*  ', end='')
    print('')
'''
'''increasing triangle'''
n = 5
for i in range(n):
    print(i * '* ')

'''decreasing triangle'''

while (n != 0):
    n -= 1
    print(n * '* ')

# right handed triangle
num = [1,2,3,4,5]
space = [5,4,3,2,1]
for x in range(len(space)):
    print(space[x]*' ', num[x]*"* ")