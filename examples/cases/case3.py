import re
regex = '^\(\d{3}\)\s\d{3}-\d{4}' 
def check(email):   
    if(re.search(regex,email)):   
        print("Valid numbers")   
    else:   
        print("Invalid numbers")
        check(input("Enter your numbers:")) 
check(input("Enter your numbers:"))