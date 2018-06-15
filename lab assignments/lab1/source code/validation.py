# importing regular expressions
import re
password= input("Input your password : ")

x = True
# this loop continues untill the value of x is false
while x:
    if (len(password)<6 or len(password)>16):
        print("Password size should be greater than 6 and less than or equal to 16")
        break
    elif not re.search("[0-9]",password):
        print("password should have atleast one digit")
        break
    elif not re.search("[$@!*]",password):
        print("password should have atleast one special character")
        break
    elif not re.search("[a-z]", password):
        print("password should have atleast one lower case letter")
        break
    elif not re.search("[A-Z]",password):
        print("password should have atleast one upper case letter")
        break
    elif re.search("\s",password):
        print("password should not contain any whitespace")
        break
    else:
        print("Valid Password")
        x=False
        break

# if all the above "if else" statements are false then the following is executed
if x:
    print("Not a Valid Password")

