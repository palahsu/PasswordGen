#Before Copy this Source, Please, Take Owner Permission and Give Credits.
#Thanks.

try:
    from string import ascii_letters, digits, punctuation, join
except ImportError:
    from string import ascii_letters, digits, punctuation
from random import choice, sample, randint
# specific imports to make this small, fast, efficient
# to generate a password with specific restrictions: \
# NO numbers or special characters in 1st position
# NO space at the end of the string

#MainFunc
def isEven(integer):
    """Return Boolean: True if input is even, False if not."""
    return integer % 2 == 0

def RandPass(size = 8):
    """This is the password generator"""
    s0 = "!@#$%^&*- _~+-=" # this set of special characters contains a space 
    s1 = ascii_letters # upper AND lower cases
    s3 = digits
    # 's0' can be CUSTOMIZED to include only allowed characters
    
    s = s0 + s1
    s_full = s + s3
    passlen = size.get()
    new_password = ""

    # assigning specific sizes for each section of the pw generated
    if isEven(passlen) == True:
        front = passlen // 5
    else:
        front = passlen // 2
    mid = 2
    previous = passlen - (front + mid) - 1

    pass0 = "".join(choice(s0)) # forces a minimum number of punctuations in the middle
    pass1 = "".join(sample(s_full,front ))
    pass2 = "".join(sample(s3,mid))
    # NO punctuations as 1st character!!! 
    pass3 = "".join(sample(s, previous ))
    # sometimes integer division reduces the size of the desired password length, the following adjusts it back
    if passlen != len(pass0 + pass1 + pass2 + pass3):
        pass2 = "".join(sample(s3,passlen - (front+previous+1) ))

    if pass3[:-1] == ' ': # to avoid having an empty space at the end of password
        temp = list(pass3)
        temp[:-1] = choice(s)
        pass3 = ''.join(str(e) for e in temp)
    new_password = pass0 + pass1 + pass2 + pass3    
    
    if passlen <= 8:
        msg = 'VERY WEAK'
        colorVal = "#6d0001"
    elif passlen <=10:
        msg = 'WEAK'
        colorVal = "#cc0000"
    elif passlen <=12:
        msg = 'DECENT'
        colorVal = "#fc8600"
    elif passlen <=14:
        msg = 'GOOD'
        colorVal = "#eae200"
    elif passlen <=16:
        msg = 'STRONG'
        colorVal = "#9ff400"
    elif passlen <=18:
        msg = 'VERY STRONG'
        colorVal = "#007715"
    elif passlen >18:
        msg = 'EXCELLENT'
        colorVal = "#001fef"
    else:
        pass

    return new_password, msg, colorVal


