import generate
from random import randint

def start(verify):


    if verify == False:
        name = str(input('Isert your name: ')).title()
        verify = True
        print('Hello {}, are you ready? \n'.format(name))
        pcNumber = randint(0, 5)

        generate.thinking()
        generate.choiceNumber(pcNumber, verify)
    else:
        verify = True
        pcNumber = randint(0, 5)

        generate.thinking()
        generate.choiceNumber(pcNumber,verify)