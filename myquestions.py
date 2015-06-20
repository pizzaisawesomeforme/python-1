import colors as c
from utils import ask

intro = c.clear + c.red + '''
'Welcome to the QUIZ game!')
''' + c.reset

def q1():
    answer = ask('What is the name of our country?')
    if answer == 'USA':
        print('We honer our country.')
        return True
    print('That is incorrect.')
    return False

def q2():
    answer = ask('Who was our first presendent?')
    if answer == 'George Washington':
        print('It is so soft.')
        return True
    print('That is incorrect.')
    return False

def q3():
    answer = ask('How many states are in our country?')
    if answer == '50':
        print('There is so many states!')
        return True
    print('That is incorrect.')
    return False

questions = [q1,q2,q3]
    
