
def factorial():
    num = int(input('enter any no. : '))
    null = 1
    for i in range(1 ,num+1):
        null = null*i
        
    print(f"the factorial of {num} is : " , null)



factorial()