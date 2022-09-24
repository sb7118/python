#WAP to find out if the input number is prime or composite

num = int(input('enter any number: '))
y=0

for x in range(1,num+1):
    if num % x == 0:
        y = y+1

if y == 2:
    print(f'{num} is a prime number!')
else:
    print(f'{num} is a composite number!')