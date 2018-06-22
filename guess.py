#!/usr/bin/env python3
import random
import sys


def valInput(playerGuess, rand, guessCount, ulam):
    '''Function used to return either the user selected integer within valid
    range or print out an error'''
    invalidOutput = "{} is invalid input"
    returnList = [True, guessCount, ulam]
    if playerGuess.isdigit():     # Checks if theres non numbers in string
        playerGuess = int(playerGuess)  # Converts to int object
        if (1 <= playerGuess <= 100):     # Verifies its within valid range
            return playGame(playerGuess, rand, returnList, ulam)
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


def playGame(playerGuess, rand, returnList, ulam):
    '''Used to check if they guess the number right and return
    high or low statement'''
    returnList[1] += 1     # Only increments with valid input
    high = "{} is to high"
    low = "{} is to low"
    if playerGuess == rand:
        returnList[0] = False
    else:
        if ulam:
            lying = amILying(returnList[1])
        else:
            lying = ulam
        if lying:
            if playerGuess < rand:
                print(high.format(playerGuess))
                returnList[2] = False
            elif playerGuess > rand:
                print(low.format(playerGuess))
                returnList[2] = False
        elif playerGuess < rand:
            print(low.format(playerGuess))
        elif playerGuess > rand:
            print(high.format(playerGuess))
    return returnList


def amILying(currentGuess):
    ulamRand = random.randint(1, currentGuess)
    if ulamRand == currentGuess:
        print("I'm Lying")
        return True


def main():
    # Checks if -u was passed to enable lying
    if len(sys.argv) == 2 and sys.argv[1] == "-u":
        ulam = True
    else:
        ulam = False
    rand = random.randint(1, 100)
    count = 0
    playing = True
    winning = "YOU WON in {} guesses."
    while playing:     # Loop until they win
        try:
            playerGuess = input("Please guess a number between 1 and 100: ")
        except (KeyboardInterrupt, EOFError):
            quitting = input("\nAre you sure you want to quit(Y/y): ")
            if quitting.lower() == "y":
                print("\nGoodbye...")
                break
            else:
                continue
        # Playing will be False unless they win, guessCount will be returned
        playing, count, ulam = valInput(playerGuess, rand, count, ulam)
        if playing is False:    # Win Condition
            if count == 1:
                print(winning.format(count).replace("guesses", "guess"))
            else:
                print(winning.format(count))

if __name__ == "__main__":
    main()
