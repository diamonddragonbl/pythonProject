import random

board = [
   '  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
   '  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
   '  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
   '  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
   '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
   '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
   '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
]

class Hangman:
   def __init__(self, word):
       self.word = word
       self.guessed_letters = []
       self.missed_letters = []

   def guess(self, letter):
       if letter in self.word and letter not in self.guessed_letters:
           self.guessed_letters.append(letter)
       elif letter not in self.word and letter not in self.missed_letters:
           self.missed_letters.append(letter)
       else:
           return False
       return True

   def hangman_over(self):
       return self.hangman_won() or (len(self.missed_letters) == 6)

   def hangman_won(self):
       if '_' not in self.hide_word():
           return True
       return False

   def hide_word(self):
       rtn = ''
       for letter in self.word:
           if letter not in self.guessed_letters:
               rtn += '_'
           else:
               rtn += letter
       return rtn

   def print_game_status(self):
       print (board[len(self.missed_letters)])
       print ('Word: ' + self.hide_word())
       print ('Incorrect guesses: '),
       for letter in self.missed_letters:
           print(letter),
       print('Correct guesses: '),
       for letter in self.guessed_letters:
           print(letter),
       print()


def rand_word():
   print("line 65")
   bank = ['house', 'halloween', 'pumpkin', 'candy', 'skeleton', 'witch', 'haunting', 'soup', 'look', 'light']
   return bank[random.randint(0, len(bank)-1)]

def main():
   game = Hangman(rand_word())
   while not game.hangman_over():
       game.print_game_status()
       user_input = input('\nEnter a letter: ')
       game.guess(user_input)

   game.print_game_status()
   if game.hangman_won():
       print('\nCongratulations! You win Hangman!')
   else:
       print('\nSorry, you have lost the game of Hangman...')
       print('The word was ' + game.word)

   if input("do you want to play Hangman again? y/n:") == 'n':
       print("thanks for playing Hangman")
       import home
       home.mane()

if __name__ == "__main__":
   main()


