import random


class Wordle:
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

   def Wordle_over(self):
       return self.Wordle_won() or (len(self.missed_letters) == 6)

   def Wordle_won(self):
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
       print ('Word: ' + self.hide_word())
       print ('Incorrect guesses: '),
       for letter in self.missed_letters:
           print(letter),


def rand_word():
   bank = ['house', 'sight', 'stove', 'candy', 'punch', 'witch', 'haunt', 'soupy', 'stock', 'light']
   return bank[random.randint(0, len(bank)-1)]

def main():
   game = Wordle(rand_word())
   while not game.Wordle_over():
       game.print_game_status()
       user_input = input('\nEnter a word: ')
       game.guess(user_input)

   game.print_game_status()
   if game.Wordle_won():
       print('\nCongratulations! You win Wordle!')
   else:
       print('\nSorry, you have lost the game of Wordle...')
       print('The word was ' + game.word)

   if input("do you want to play Wordle again? y/n:") == 'n':
       print("thanks for playing Wordle")
       print('============================')
       import homey
       homey.mane('x')
   else:
       main()

if __name__ == "__main__":
   main()
