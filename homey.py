app_number = 2

def start():
    password = 'Ben_is_cool'
    signing_in_or_making_account = input('are you signing in or making an account:')
    if signing_in_or_making_account == 'signing in':
        code = input('code:')
        if code == password:
             mane()
    else:
        binary = input('what is 23 in binary:')
        if binary == '11101':
            password = input('what would you like your password to be:')
            code = input('password:')
            if code == password:
                mane()

def mane():
    print(f'welcome to the home page. we have {app_number} apps')

    answer = input('do you want to play Hangman or use a calculator:')
    if answer == 'Hangman':
        import hangman1
        hangman1.main()
    else:
        import calculator
        calculator.calculator_run()

if __name__ == "__main__":
   start()