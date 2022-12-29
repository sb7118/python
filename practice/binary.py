'''WAP to convert the string input by the user in binary'''
text = input("enter any text : ")

#bin() and int.from_bytes() .. variable.encode() , 'big'
binary = bin(int.from_bytes(text.encode() , 'big'))
print(binary)