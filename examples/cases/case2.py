import re
regex = '^[a-zA-Z0-9]{3,10}\w+[@]+[a-zA-Z0-9]{2,10}\w+[.]\w[a-z]{2,3}$'  
def check(email):   
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   
check(input("Enter your email adress:"))