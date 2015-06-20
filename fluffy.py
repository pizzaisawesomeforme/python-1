import colors as c
from utils import ask

intro = c.clear + c.magenta + '''
'Welcome to the QUIZ game!')
''' + c.reset

def q1():
    answer = ask('What are the color of the unicorns?')
    if answer == 'pink':
        print('And what a lovely color it is.')
        return True
    print('That is incorrect.')
    return False

def q2():
    answer = ask('What texture were the unicorns?')
    if answer == 'cotton':
        print('It is so soft.')
        return True
    print('That is incorrect.')
    return False

def q3():
    answer = ask('What were the unicorns doing?')
    if answer == 'dancing':
        print('Dancing is so much FUN!')
        return True
    print('That is incorrect.')
    return False

questions = [q1,q2,q3]
    
