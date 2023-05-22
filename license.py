

def chklic(i):
    try:
        f = open('licence.atmlic', 'r')
        return True
    except:
        return False


def decode(i):
    cipher = open('licence.atmlic', 'r').read()
    for i in range(26):
        plain = ''
        for c in cipher:
            if c.isalpha():
                plain += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
            else:
                plain += c
        if "valid" in plain:
            return True 
def lic (i):
    lic_present = chklic(i)
    if lic_present == True:
        validity = decode(i)
        if validity == True:
            return True
        else:
            return False
    else:
        return False
