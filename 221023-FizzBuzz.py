

# Constants

HELLO = '''
        Welcome to FizzBuzz
        If the number printed can evenly
        be devided by
        > 3 : Enter Fizz
        > 5 : Enter Buzz
        > 3 AND 5 : FizzBuzz
        otherwise just press <Enter>

        Comparing only the first 2 chars (tolower)

'''

# Variables

count = 0
FizzBuzz = ''

# Functions

def getAnswer(number):

    # valid returns:
    # Fizz, Buzz, FizzBuzz, ''

    fizz = ''
    buzz = ''
    if not number % 3:
        fizz = True
    if not number % 5:
        buzz = True
    if fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return ''

def matchUserInput(count,uIn):
    return (count == uIn)

def finishGame(count):
    print(f'''
        !!! mööp !!!
        Du hattest immerhin {count-1}
        erfolgreiche Eingaben :D 
    ''')

    # set finish condition
    count = -1


# ################
# Main
# ################

print(HELLO)

while count > -1:
    count +=1
    answer = getAnswer(count)

    userInput = input(f">{count}:")

    if not matchUserInput(answer, userInput):
        finishGame(count)
        

    
