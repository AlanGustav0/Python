import generate
from random import randint


def start(first_time):
    if first_time:
        name = str(input('Insert your name: ')).title()
        first_time = False
        print('Hello {}, are you ready? \n'.format(name))
    pc_number = randint(0, 5)
    generate.thinking()
    generate.choice_number(pc_number, first_time)
