def number_only(input):
    try:
        # Convert it into integer
        val = int(input)
    except ValueError:
        print("No.. input is not a number. Start over.")
        calculator_run()

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
    a = str(input("Enter first number:"))
    number_only(a)
    a_int = int(a)
    b = str(input("Enter second number:"))
    number_only(b)
    b_int = int(b)

    sum = adding(a_int, b_int)

    print(f"{a} plus {b} is {sum}")

def play_subtract():
    print('============================')
    a = str(input("Enter first number:"))
    number_only(a)
    a_int = int(a)
    b = str(input("Enter second number:"))
    number_only(b)
    b_int = int(b)

    sum = subtracting(a_int, b_int)

    print(f"{a} plus {b} is {sum}")

def play_multiply():
    print('============================')
    a = str(input("Enter first number:"))
    number_only(a)
    a_int = int(a)
    b = str(input("Enter second number:"))
    number_only(b)
    b_int = int(b)

    sum = multiply(a_int, b_int)

    print(f"{a} plus {b} is {sum}")

def play_divide():
    print('============================')
    a = str(input("Enter first number:"))
    number_only(a)
    a_int = int(a)
    b = str(input("Enter second number:"))
    number_only(b)
    b_int = int(b)

    sum = divide(a_int, b_int)

    print(f"{a} plus {b} is {sum}")

def calculator_run():
    while True:
        print('============================')
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
            homey.mane('x')
        else:
            print ('what are you doing? stop breaking my calculator!')
        if input("do you want to do math again? y/n:") == 'n':
            print("thanks for using Ben's calculator")
            import homey
            homey.mane('x')

if __name__ == "__main__":
   calculator_run()