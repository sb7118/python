'''WAP to find the LCM of two numbers'''
#to find the greatest number
def lcm(num1, num2):
    if num1 > num2:
        greater = num1 #12
    else:
        greater = num2 #14
    
    while True:
        if(greater % num1 ==0) and (greater % num2 == 0): #conclusion :  the integer "greater" keeps incrementing until when both intergers (num1 and num2) gets remainder 0 . and the loops will terminate and returns the last value of "greater".
            break
        greater +=1
    return greater

print(f"lcm = {lcm(12,14)}")