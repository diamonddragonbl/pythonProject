app_number = 2
home_screen1 = '        __________________'
home_screen2 = '        |                |'
home_screen3 = '        |                |'
home_screen4 = '        |                |'
home_screen5 = '        |                |'
home_screen6 = '==================================='
answer_home_screen = 'Magicians hat'
def start():
    password = 'Ben_is_cool'
    signing_in_or_making_account = input('are you signing in or making an account:')
    if signing_in_or_making_account == 'signing in':
        code = input('password:')
        if code == password:
             mane('H')
    elif signing_in_or_making_account == '/skip':
        mane('n')
    else:
        binary = input('what is 23 in binary:')
        if binary == '11101':
            password = input('what would you like your password to be:')
            code = input('password:')
            if code == password:
                mane('n')

def mane_again():
    answer = input('but we do have Hangman or a calculator:')
    if answer == 'Hangman' or answer == 'hangman':
        import hangman1
        hangman1.main()
    elif answer == 'Calculator' or answer == 'calculator':
        import calculator
        calculator.calculator_run()
    else:
        print('sorry we do not have that game...')
        mane_again()

def mane(returning):
    if returning != 'x':
        print(f"{home_screen1}")
        print(f'{home_screen2}')
        print(f'{home_screen3}')
        print(f'{home_screen4}')
        print(f'{home_screen5}')
        print(f'{home_screen6}')

    print(f'welcome to the home page. we have {app_number} apps')

    print('type home screen to chang the photo on your home screen')
    answer = input('do you want to play Hangman or use a calculator:')
    if answer == 'Hangman' or answer == 'hangman':
        import hangman1
        hangman1.main()
    elif answer == 'Calculator' or answer == 'calculator':
        import calculator
        calculator.calculator_run()
    elif answer == 'home screen' or answer == 'Home screen' or answer == 'home Screen' or answer == 'Home Screen':
        answer_home_screen = input('do you wont your home screen to be a magicians hat or a wand:')
        if answer_home_screen == 'magicians hat' or answer_home_screen == 'Magicians hat' or answer_home_screen == 'magicians Hat' or answer_home_screen == 'Magicians Hat':
            print('ok')
            print('        __________________')
            print('        |                |')
            print('        |                |')
            print('        |                |')
            print('        |                |')
            print('===================================')
            mane('x')
        elif answer_home_screen == 'wand' or answer_home_screen == 'Wand':
            print()
            print('||===========================||')
            print('||                           ||')
            print('||===========================||')
            print()
            mane('x')
    else:
        print('sorry we do not have that game...')
        mane_again()

if __name__ == "__main__":
   start()