def Fibo():

    previous = 1
    current = 2
    auxiliary = 0

    count = 0

    print('0 - 1 - 1')

    while count < number:

        next = current + previous

        print('- {}',end=' '.format(next))

        previous = current
        current = next

        count += 1


        
        
number = (int(input('Isert the number')))

Fibo(number)

