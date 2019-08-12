import string

def SimplePassword(str): 

    # get password
    password = str

    # conditions initial values
    cond1 = False
    cond2 = False
    cond3 = False
    cond4 = False
    
    # check conditions of individual characters (Conditions 1, 2 and 3)
    for letter in password:
        if letter.isupper():
            cond1 = True
        if letter.isdigit():
            cond2 = True
        if letter in string.punctuation:
            cond3 = True
    
    # check "password" string is not in password (Condition 4)
    if "password" not in password.lower():
        cond4 = True
    
    # check password length satisfies (Condition 5)
    if (len(password) > 7 and len(password) < 30):
        cond5 = True
    else:
        cond5 = False
    
    # check all conditions are satisfied
    if (cond1 and cond2 and cond3 and cond4 and cond5):
        return "true"
    else:
        return "false"
    
# keep this function call here  
print SimplePassword(raw_input())