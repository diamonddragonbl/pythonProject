import settings

app_number = 2
home_screen1 = '        __________________'
home_screen2 = '        |                |'
home_screen3 = '        |                |'
home_screen4 = '        |                |'
home_screen5 = '        |                |'
home_screen6 = '==================================='

def start():
    password = 'Ben_is_cool'
    signing_in_or_making_account = input('are you signing in or making an account:')
    if signing_in_or_making_account == 'signing in':
        code = input('password:')
        if code == password:
             mane('x')
    elif signing_in_or_making_account == '/skip':
        mane('x')
    else:
        binary = input('what is 23 in binary:')
        if binary == '11101':
            password = input('what would you like your password to be:')
            code = input('password:')
            if code == password:
                mane('x')

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
    if settings.answer_home_screen == 'magicians hat' or settings.answer_home_screen == 'Magicians hat' \
            or settings.answer_home_screen == 'magicians Hat' or settings.answer_home_screen == 'Magicians Hat':

        print(f"{home_screen1}")
        print(f'{home_screen2}')
        print(f'{home_screen3}')
        print(f'{home_screen4}')
        print(f'{home_screen5}')
        print(f'{home_screen6}')
    else:

        print()
        print('||===========================||')
        print('||                           ||')
        print('||===========================||')


    print(f'welcome to the home page. we have {app_number} apps')
    print('type home screen to change the photo on your home screen')
    answer = input('do you want to play Hangman or use a calculator:')
    if answer == 'Hangman' or answer == 'hangman':
        import hangman1
        hangman1.main()
    elif answer == 'Calculator' or answer == 'calculator':
        import calculator
        calculator.calculator_run()
    elif answer == 'home screen' or answer == 'Home screen' or answer == 'home Screen' or answer == 'Home Screen':
        settings.answer_home_screen = input('do you wont your home screen to be a magicians hat or a wand:')
        if settings.answer_home_screen == 'magicians hat' or settings.answer_home_screen == 'Magicians hat' \
                or settings.answer_home_screen == 'magicians Hat' or settings.answer_home_screen == 'Magicians Hat':
            mane('x')
        elif settings.answer_home_screen == 'wand' or settings.answer_home_screen == 'Wand':
            mane('x')
    else:
        print('sorry we do not have that game...')
        mane_again()

if __name__ == "__main__":
   start()