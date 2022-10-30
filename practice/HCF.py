'''WAP to find the HCF of any two numbers'''
#to find the smallest number
def HCF(num1,num2):
    if num2>num1:
        smallest = num1
    else:
        smallest = num2
    #looping from 1 to the smallest number
    for i in range(1,smallest+1):
        if num1%i==0 and num2%i==0:
            HCF = i
    return HCF
        
print(HCF(24,60))