"""
Fibonacci Sequence

Enter a number and have the program generate the Fibonacci sequence to that
number or to the Nth number.
"""


def calc_fibonacci(number):

    a = 1
    b = 1

    for i in range(1, number + 1):

        yield (i,a)

        a, b = b, a + b


def new_calc():

    global running

    while True:

        user_input = input('\nDo you want to calculate a new Fibonacci sequence? "y" / "n"\n')

        if user_input[0].lower() == 'y':
            break

        elif user_input[0].lower() == 'n':
            print("\nBye now!")
            running = False

        else:
            print('\nSorry, please try again:')
            continue

        break


print("\n\t\t***** Welcome to the Fibonacci sequence Calculator *****")

running = True

while running:

    try:

        user_input = int(input('\nPlease enter a number and I will calculate the Fibonacci sequence to that number: '))


        for i,fib in calc_fibonacci(user_input):

            print(str(f'The Fibonacci number of {i} is:' + '\t' + str(fib)))

        new_calc()

    except:

        print('\nThis was not a valid number!')
        continue