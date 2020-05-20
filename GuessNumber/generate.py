from GuessNumber import rules


def generateNumber(pcNumber):

    value = 10 ** 7
    print('Just a moment, I\'ll think of a number... \n')

    for i in range(0, value):
        i *= 2 * value
    print('Great! \n')

    choiceNumber(pcNumber)


def choiceNumber(pcNumber):

    statusOk = False

    while statusOk == False:

        try:
            number = int(input('Well, what number did I think? Insert a number 0 to 5:  '))
            if (number < 0 or number > 5):
                print('Invalid number!')
            else:
                rules.remake(number, pcNumber)
        except ValueError:
            print('Invalid option!')