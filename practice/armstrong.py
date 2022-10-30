'''
    armstrong number checker . 
    like: 153 == 1**3 + 5**3 + 3**3
          153 == 153
'''
num = int(input('enter any number : '))
copy_num = num #to save the value of num for future conditional statement
remainder = 0
order = len(str(num))
sum = 0
while(num!=0):
    remainder = num % 10
    sum += remainder ** order
    num = num//10   
    '''
    num = num/10 : it'll return float.
    so , num = num // 10  returns integer part only 
    '''
if(sum==copy_num):
    print("armstrong number")
else:
    print("not a armstrong number")