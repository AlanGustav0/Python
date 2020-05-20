import generate
from random import randint

def start():
    name = str(input('Isert your name: ')).title()

    print('Hello {}, are you ready? \n'.format(name))
    pcNumber = randint(0, 5)

    generate.generateNumber(pcNumber)
    generate.choiceNumber()

start()

