import generate


def validate(valid):

    if (valid.isalpha() == True and valid == "y"):
        tryAgain = True
        generate.generateNumber(tryAgain)

    elif valid.isalpha() == True and valid == "n":
        print('Good Bye!')
        exit()

    else:
        print('Invalid option')

def remake(number, pcNumber):
    done = False

    if number == pcNumber:
        print('You win! It was this number! \n')
        while done == False:
            valid = str(input('Do you want try again? Insert (Y) for Yes and ?(N) for No: ')).lower()
            validate(valid)
    else:

        print('Oops, you lose! The number is {} try again!\n'.format(pcNumber))
        while done == False:
            valid = str(input('Do you want try again? Insert (Y) for Yes and ?(N) for No: ')).lower()
            validate(valid)






