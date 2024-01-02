import random

NUM_DIGITS = 3
MAX_GUESSES = 10 

def main():
  print('''bagels, a deductive logic game.
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
  Pico      One digit is correct but in the wrong position.
  Fermi     One digit is correct and in the right position.
  Bagels    No digit is correct.

For example, if the secret number was 248 and your guess 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))
  
  while True:   # main game loop.
    # this storest the secret number players needs to guess:
    secretNum = getSecretNum()
    print('i have thought up a number.')
    print(' you have {} guesses to get it.'.format(MAX_GUESSES))

    num_Guesses = 1
    while num_Guesses <= MAX_GUESSES:
      guess = ''
      # keep looping until they enter a valid guess:
      while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print('Guess # {}: '.format(num_Guesses))
        guess = input('> ')
      
      clues = getClues(guess, secretNum)
      print(clues)
      num_Guesses += 1

      if guess == secretNum:
        break # they're correct, so break out of this loop.
      if num_Guesses > MAX_GUESSES:
        print('you ran out of guesses.')
        print('the answer was {}.'.format(secretNum))
    
    # ask player if they want to play again.
    print('do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
      break
  print('thanks for playing!')


def getSecretNum():
  # returns a string made up of NUM_DIGITS unique random digits.
  numbers = list('0123456789')    # create a list of digits 0 to 9.
  random.shuffle(numbers)   # shuffle them into random order.

  # get the first NUM_DIGITS digits in the list for the secret number:
  secretNum = ''
  for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
  return secretNum

def getClues(guess, secretNum):
  '''returns a string with the pico, fermi, bagels clues for a guess
  and secret number pair.'''
  if guess == secretNum:
    return 'you got it!'
  
  clues = []

  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      # a correct digit is in the correct place.
      clues.append('Fermi')
    elif guess[i] in secretNum:
      # a correct digit is in the incorrect place.
      clues.append('Pico')
  if len(clues) == 0:
    return 'Bagels'   # there are no correct digits at all.
  else:
    # sort the clues into alphabetical order so their original order
    # doesn't give information away.
    clues.sort()
    # make a single string from the list of string clues.
    return ' '.join(clues)


# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
  main()