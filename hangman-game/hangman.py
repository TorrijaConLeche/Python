# This program may have errors, it was made to learn Python.

import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def random_word():  # Pick a random word in the list

    words = ["Abnormal", "Elucidate", "Pacify", "Query", "Queue",
             "Quiet", "Rapid", "Stationary", "Uproarious", "Urgent"]

    target = random.choice(words)

    return (list(target))


print("Welcome to the Hangman !")
print("------------------------")

while True:
    action = input("\nDo you want to play? (Y / N)")
    if action.lower() == "n":
        break

    # random_word() Pick a random word using the function

    target = random_word()  # Pick a random word using the function

    target_hidden = list("_"*len(target))
    print("")
    print(" ".join(target_hidden))

    fails = 0  # Track when user input is wrong

    while target != target_hidden:
        user_letter = input("\nInput a letter: ")
        if user_letter in target:

            cont = 0  # Used to track index number

            for t in target:  # Reemplaza solo una letra

                if user_letter == t:
                    target_hidden[cont] = user_letter  # Replace _ to a letter
                    print("\n Correct!")

                cont += 1  # Tracking index

            print("\n", " ".join(target_hidden))

            if target == target_hidden:
                print("\nYou've won the game!\n")

        else:
            if fails < (len(HANGMANPICS) - 1):
                print(HANGMANPICS[fails])
                print("Wrong!")
                fails += 1  # Used to iterate into the ascii art hangman pics

            else:
                print("\nGame over, the word was", "".join(target))
                break
