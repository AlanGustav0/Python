import start


def validate(valid, verify):
    if valid.isalpha() and valid == "y":
        start.start(verify)
    elif valid.isalpha() and valid == "n":
        print('Good Bye!')
        exit()
    else:
        print('Invalid option')


def remake(number, pc_number, verify):
    done = False
    if number == pc_number:
        print('You win! It was this number! \n')
    else:
        print('Oops, you lose! The number was {} try again!\n'.format(pc_number))
    while not done:
        valid = str(input('Do you want try again? Insert (Y) for Yes and ?(N) for No: ')).lower()
        validate(valid, verify)
