#!/usr/bin/env python3
import random


def inputVal(check, rand, guessCount):
    '''Function used to return either the user selected integer within valid
    range or print out an error'''
    invalidOutput = "{} is invalid input"
    if check.isdigit():     # Checks if theres non numbers in string
        check = int(check)  # Converts to int object
        if (1 <= check <= 100):     # Verifies its within valid range
            return checkInput(check, rand, guessCount)
        else:
            print(invalidOutput.format(check))
            return True, guessCount
    else:
        print(invalidOutput.format(check))
        return True, guessCount


def checkInput(selection, rand, guessCount):
    '''Used to check if they guess the number right and return
    high or low statement'''
    guessCount += 1     # Only increments with valid input
    if selection == rand:
        return False, guessCount
    else:
        if selection < rand:
            print(selection, "is to low. ")
            return True, guessCount
        else:
            print(selection, "is to high. ")
            return True, guessCount


def main():
    rand = random.randint(1, 100)
    guessCount = 0
    playing = True
    winning = "YOU WON in {} guesses."
    while playing:     # Loop until they win
        try:
            selection = input("Please guess a number between 1 and 100: ")
        except (KeyboardInterrupt, EOFError):
            print()
            break
        # Playing will be False unless they win, guessCount will be returned
        playing, guessCount = inputVal(selection, rand, guessCount)
        if playing is False:    # Win Condition
            if guessCount == 1:
                print(winning.format(guessCount).replace("guesses", "guess"))
            else:
                print(winning.format(guessCount))

if __name__ == "__main__":
    main()
