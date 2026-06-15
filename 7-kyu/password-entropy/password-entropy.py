import math
​
def entropy(password):
    lower = False
    upper = False
    number = False
    special = False
    for letter in password:
        if letter.islower():
            lower = True
        if letter.isupper():
            upper = True
        if letter.isdigit():
            number = True
        if not letter.isalnum():
            special = True
    R = 0
    
    if lower:
        R += 26
    if upper:
        R += 26
    if number:
        R += 10
    if special:
        R += 32
        
    L = len(password)
    
    E = L * math.log2(R)
    
    return E
    