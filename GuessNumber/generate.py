import rules
from time import sleep


def thinking():
    print('Just a moment, I\'ll think of a number... \n')
    sleep(2)
    print('Great! \n')


def choice_number(pc_number, verify):
    status_ok = False
    while not status_ok:
        try:
            number = int(input('Well, what number did I think? Insert a number 0 to 5:  '))
            if number < 0 or number > 5:
                print('Invalid number!')
            else:
                rules.remake(number, pc_number, verify)
        except ValueError:
            print('Invalid option!')
