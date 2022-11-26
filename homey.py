app_number = 2

def start():
    password = 'Ben_is_cool'
    signing_in_or_making_account = input('are you signing in or making an account:')
    if signing_in_or_making_account == 'signing in':
        code = input('password:')
        if code == password:
             mane()
    elif signing_in_or_making_account == '/skip':
        mane()
    else:
        binary = input('what is 23 in binary:')
        if binary == '11101':
            password = input('what would you like your password to be:')
            code = input('password:')
            if code == password:
                mane()

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

def mane():
    print(f'welcome to the home page. we have {app_number} apps')

    answer = input('do you want to play Hangman or use a calculator:')
    if answer == 'Hangman' or answer == 'hangman':
        import hangman1
        hangman1.main()
    elif answer == 'Calculator' or answer == 'calculator':
        import calculator
        calculator.calculator_run()
    else:
        print('sorry we do not have that game...')
        mane_again()

if __name__ == "__main__":
   start()