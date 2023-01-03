
import random

def rand_word():
    bank = ['house', 'halloween', 'pumpkin', 'candy', 'skeleton', 'witch', 'haunting', 'soup', 'look', 'light']
    the_word = bank[random.randint(0, len(bank)-1)]
    return (the_word)

def hide_word(self):
    rtn = ''
    for letter in self.word:
        if letter not in self.guessed_letters:
            rtn += '_'
        else:
            rtn += letter
    return rtn

def main():
    guess = input(':')
    print(hide_word(guess))

if __name__ == "__main__":
    main()