import colors as c

def ask(question):
    print(c.red + question + c.reset) 
    answer = input("> " + c.base3).lower().strip()
    print(c.reset)
    return answer
