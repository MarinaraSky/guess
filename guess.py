#!/usr/bin/env python3
import random


def validateInput(playerGuess, rand, guessCount):
    '''Function used to return either the user selected integer within valid
    range or print out an error'''
    invalidOutput = "{} is invalid input"
    returnList = [True, guessCount]
    if playerGuess.isdigit():     # Checks if theres non numbers in string
        playerGuess = int(playerGuess)  # Converts to int object
        if (1 <= playerGuess <= 100):     # Verifies its within valid range
            return playGame(playerGuess, rand, returnList)
        else:
            invalidInput(playerGuess)
            return returnList
    else:
        invalidInput(playerGuess)
        return returnList


def invalidInput(playerGuess):
    '''Function to output invalid input string'''
    invalidOut = "{} is invalid input."
    print(invalidOut.format(playerGuess))


def playGame(playerGuess, rand, returnList):
    '''Used to check if they guess the number right and return
    high or low statement'''
    returnList[1] += 1     # Only increments with valid input
    if playerGuess == rand:
        returnList[0] = False
    else:
        if playerGuess < rand:
            print(playerGuess, "is to low. ")
        else:
            print(playerGuess, "is to high. ")
    return returnList


def main():
    rand = random.randint(1, 100)
    guessCount = 0
    playing = True
    winning = "YOU WON in {} guesses."
    while playing:     # Loop until they win
        try:
            playerGuess = input("Please guess a number between 1 and 100: ")
        except (KeyboardInterrupt, EOFError):
            print()
            break
        # Playing will be False unless they win, guessCount will be returned
        playing, guessCount = validateInput(playerGuess, rand, guessCount)
        if playing is False:    # Win Condition
            if guessCount == 1:
                print(winning.format(guessCount).replace("guesses", "guess"))
            else:
                print(winning.format(guessCount))

if __name__ == "__main__":
    main()
