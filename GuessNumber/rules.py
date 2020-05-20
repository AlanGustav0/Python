import start


def validate(valid,verify):

    if (valid.isalpha() == True and valid == "y"):
        start.start(verify)

    elif valid.isalpha() == True and valid == "n":
        print('Good Bye!')
        exit()

    else:
        print('Invalid option')

def remake(number, pcNumber,verify):
    done = False

    if number == pcNumber:
        print('You win! It was this number! \n')
        while done == False:
            valid = str(input('Do you want try again? Insert (Y) for Yes and ?(N) for No: ')).lower()
            validate(valid,verify)
    else:

        print('Oops, you lose! The number is {} try again!\n'.format(pcNumber))
        while done == False:
            valid = str(input('Do you want try again? Insert (Y) for Yes and ?(N) for No: ')).lower()
            validate(valid,verify)








