''' simple python password generator '''
import random

string = 'qwertyuioplkjhgfdsazxcvbnm'
numbers = '1234567890'
symbol = '!@#$%^&*()_+}{|":>?<>'

#container for str ,num & symbols
list = string + numbers + symbol

password = ''
for i in range(1 ,10+1):
    password = password + list[random.randint(1 , len(list))]

print(password)