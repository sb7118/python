def string(str):
    result= ""
    i = len(str)-1
    while(i > -1):
        result += str[i]
        i += -1
    print(result)
        
    
str = input("enter any string : ")
string(str) 