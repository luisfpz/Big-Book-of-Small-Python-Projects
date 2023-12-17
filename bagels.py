import random

NUM_DIGITS = 3 # change later to see changes
MAX_GUESSES = 10 # change later to see changes

def main():
  print('''Bagels, a detective logic game.
        I am thinking of a {}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        When I say:     That means:
        Pico            One digit is correct but in the wrong position.
        Fermi           One digit is correct and in the right postion.
        Bagels          No digit is correct.

        For example, if the secret number was 248 and your guess was 843, the 
        clues would be Fermi Pico.'''.format(NUM_DIGITS))
  
  while True:   # main game loop.
    # This stores the secret number the player needs to guess:
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print('You have {} guesses to get it.'.format(MAX_GUESSES))

    numGuesses = 1
    while numGuesses  <= MAX_GUESSES:
      guess = ''
      # Keep looping until they enter a valid guess:
      while len(guess)  !=  NUM_DIGITS or not guess.isdecimal():
        print('Guess #{}: '.format(numGuesses))
        guess = input('> ')
      
      clues = getClues(guess, secretNum)
      print(clues)
      numGuesses += 1

      if guess == secretNum:
        break # they're correct, so break out of this loop
      if numGuesses > MAX_GUESSES:
        print('You ran out of guesses.')
        print('The answer was {}.'.format(secretNum))
    
  # ask player if they want to play again.
    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
      break
    print('Thanks for playing!')

def getSecretNum():
  '''Returns a string made up of NUM_DIGITS unique random digits.'''
  numbers = list('0123456789')  # create a list of digits 0 to 9
  random.shuffle(numbers)   # shuffle them into random order.

  # get the first NUM_DIGITS digits in the list for the secret number:

  secretNum = ''
  for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
  return secretNum

def getClues(guess, secretNum):
  '''Returns a string with the pico, fermi, bagels clues for a guess
  and secre number pair.'''
  if guess == secretNum:
    return 'You got it!'
  
  clues = []

  for i in range(len(guess)):
    if guess[i] ==  secretNum[i]:
      # a correct digit is in the correct place
      clues.append('Fermi')
    elif guess[i] in secretNum:
      # a correct digit is in the incorrect place
      clues.append('Pico')
  if len(clues) ==  0:
    return 'Bagels'   # there are no correct digits at all.
  else:
    # sortthe clues into alphabetical order so their original order
    # doesn't give information away.
    clues.sort()
    # make a singe string from the list of string clues
    return ' '.join(clues)
  
# if the program is run (instead of imported), run the game:
if __name__  ==  '__main__':
  main()