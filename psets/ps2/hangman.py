# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter  not in letters_guessed:
            return False
    return True
        


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
    guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    progress = ''
    for letter in secret_word:
        if letter in letters_guessed:
            progress += letter
        else:
            progress += '*'
    return progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

def reveal_letter(secret_word, available_letters):
    """
    secret_word: string, the lowercase word the user is guessing
    available_letters: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
    guessed so far
    
    returns: string, a single character randomly chosen from unique letters
    that are both in secret_word and available_letters
    
    """
    choose_from = ''
    for letter in secret_word:
        if letter in available_letters and letter not in choose_from:
            choose_from += letter
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter
                
def count_unique(secret_word):
    """
    secret_word : secret_word: string, the lowercase word the user is guessing
    available_letters: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
    guessed so far

    Returns number of unique letters in secret_world

    """     
    exist = []
    for char in secret_word:
        if char not in exist:
            exist.append(char)
    return len(exist)

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    num_guesses = 10
    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)
    progress = get_word_progress(secret_word, letters_guessed)
    while num_guesses > 0 and not has_player_won(secret_word,letters_guessed): 
       
        print('--------------')
        print(f'You have {num_guesses} guesses left.')
        print('Available letters: '+ available_letters)
        guess = input('Please guess a letter: ')
        # Case 1: help case
        if with_help and guess == '!':
            # Case 1a: if num_guesses at least 3, give the help
            if num_guesses >= 3: 
                revealed_letter = reveal_letter(secret_word, available_letters)
                letters_guessed.append(revealed_letter)
                available_letters = get_available_letters(letters_guessed)
                progress = get_word_progress(secret_word, letters_guessed)
                num_guesses -= 3
                print('Letter revealed: ' + revealed_letter)
                print(progress)
            # Case 1b: if not enough guesses, give warning
            else:
                print('Oops! Not enough guesses left: ' + progress)
        # Case 2: invalid input, give warning
        elif len(guess) != 1 or not guess.isalpha():
            print('Oops! That is not a valid letter. Please input a letter from ')
            print('the alphabet: ' + progress)
        # Case 3 (main case): valid input, cast to lowercase
        else:
            guess = guess.lower()
            # Case 3a: if the letter has been guessed before, progress is not changed, num_guessess not changed
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter: " + progress)
            # Case 3b: it is a new letter, assess further conditions
            else:
                letters_guessed.append(guess)
                available_letters = get_available_letters(letters_guessed)
                # Case 3b(i): guess is not correct, progress is not changed, update num_of_guesses by vowel/consonant rule
                if guess not in secret_word:
                    print('Oops! That letter is not in my word: ' + progress)
                    if guess not in 'aeiou':
                        num_guesses -= 1
                    else:
                        num_guesses -= 2
                # Case 3b(ii): if guess is correct, update progress, num_guessess not changed
                else:
                    progress = get_word_progress(secret_word, letters_guessed)
                    print('Good guess: ' + progress)
    # if num_guesses = 0 and not all letters are guessed, the player loses
    if num_guesses == 0 and not has_player_won(secret_word,letters_guessed):
        print('--------------')
        print('Sorry, you ran out of guesses. The word was ' + secret_word)
    # otherwise, the player wins
    else:
        print('--------------')   
        print('Congratulations, you won!')
        score = num_guesses + 4*count_unique(secret_word) + 3*len(secret_word)
        print(f'Your total score for this game is: {score}')
            
                
            
             
           
            
            
            
        
            
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.
    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

     

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

