#WAP to write the accronym of input phrases for example : central processing unit = CPU
user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
print(text) #shows the splited list of strings