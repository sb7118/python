#WAP to get the username and domain name from input email
email = input("Enter Your Email: ").strip() #.strip() remover whitespaces from the input
username = email[:email.index("@")] #email.index() will be terminated before reaching @
domain_name = email[email.index("@")+1:] 
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)
