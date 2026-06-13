
email = input("Enter your email address: ")
if "@" in email and "." in email:  
    at_pos = email.index("@")
    dot_pos = email.rindex(".")
    if at_pos > 0 and dot_pos > at_pos + 1:
        print("Valid Email Address")
    else:
        print("Invalid Email Address")
else:
    print("Invalid Email Address")