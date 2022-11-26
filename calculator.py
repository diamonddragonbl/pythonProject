
def adding(a, b):
    return a + b

def subtracting(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def play_add():
    print('============================')
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    sum = adding(a, b)

    print(f"{a} plus {b} is {sum}")

def play_subtract():
    print('============================')
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    sum = subtracting(a, b)

    print(f"{a} minus {b} is {sum}")

def play_multiply():
    print('============================')
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    sum = multiply(a, b)

    print(f"{a} times {b} is {sum}")

def play_divide():
    print('============================')
    a = input("Enter first number:")
    b = input("Enter second number:")

#    if a.isnumeric():
#        print('what do to')
#    else:
#        print('You must enter only numbers.')
#        a = input("Enter first number:")

    sum = divide(a, b)

    print(f"{a} divided by {b} is {sum}")

def calculator_run():
    while True:
        answer = input("do you want to add, subtract, divide or multiply?:")
        if answer == 'add' or answer == 'a':
            play_add()
        elif answer == 'subtract' or answer == 's':
            play_subtract()
        elif answer == 'multiply' or answer == 'm':
            play_multiply()
        elif answer == 'divide' or answer == 'd':
            play_divide()
        elif answer == 'stop':
            print("thanks for using Ben's calculator")
            import homey
            homey.mane()
        else:
            print ('what are you doing? stop breaking my calculator!')
        if input("do you want to do math again? y/n:") == 'n':
            print("thanks for using Ben's calculator")
            import homey
            homey.mane()

if __name__ == "__main__":
   calculator_run()