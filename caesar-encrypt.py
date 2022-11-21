
from string import ascii_letters

# Constants

HELLO = '''
        Welcome to Caesar Encrypt / Decrypt
'''

GETMODE = '''
        (e)ncrypt or (d)ecrypt?
        leave empty to end
'''

GETSHIFT = '''
        How many chars is the shift? 
'''

GETSTRING = '''
        Whats the string? 
'''

# Variables

mode = "x"

def getMode():
    print(GETMODE)
    mode = input()
    if mode:
        return(mode)
    else:
        exit(0)

def getShift():
    print(GETSHIFT)
    return(input())

def getStr():
    print(GETSTRING)
    return(input())

def encrypt(s: str,shift: int):
    # s='Surjudpplhuxqj lvw hlqidfk qxu phjd jxw'
    ns=''
    for c in s:
        if c in ascii_letters:
            ns=ns+ascii_letters[(ascii_letters.index(c)+shift)%len(ascii_letters)]
        else:
            ns+=c

    print(ns)

def decrypt(s: str,shift: int):
    # s='Surjudpplhuxqj lvw hlqidfk qxu phjd jxw'
    ns=''
    for c in s:
        if c in ascii_letters:
            ns=ns+ascii_letters[(ascii_letters.index(c)+shift)%len(ascii_letters)]
        else:
            ns+=c

    print(ns)


# ################
# Main
# ################

print(HELLO)

while mode:
    mode = getMode()
    origStr = getStr()
    shift = int(getShift())

    match mode:
        case 'e':
            encrypt(origStr,shift)

        case 'd':
            decrypt(origStr,-abs(shift))

