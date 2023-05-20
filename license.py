

def chklic(i):
    try:
        f = open('licence.atmlic', 'r')
        f.close()
        return True
    except:
        return False

def decode(cipher):
    cipher = open('licence.atmlic', 'r').read()
    for i in range(26):
        plain = ''
        for c in cipher:
            if c.isalpha():
                plain += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
            else:
                plain += c
        if valid in plain:
            return True 
        print(plain)

licchk = chklic(0)

if licchk == True:
    decode(licchk)