#!/usr/bin/env python3
import random
import sys


def valInput(playerGuess, returnList, rand):
    '''Function used to return either the user selected integer within valid
    range or print out an error'''
    invalidOutput = "{} is invalid input"
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
    high = "{} is to high"
    low = "{} is to low"
    if playerGuess == rand:
        returnList[0] = False
    else:
        if returnList[2]:   # This is checking if Ulam's game is enabled
            lying = amILying(returnList[1])  # Using the attempt number to lie
        else:
            lying = returnList[2]   # Ulam's not enabled
        if lying:
            if playerGuess < rand:
                print(high.format(playerGuess))
                returnList[3] = high.format(playerGuess).replace("is", "was")
            elif playerGuess > rand:
                print(low.format(playerGuess))
                returnList[3] = low.format(playerGuess).replace("is", "was")
            returnList[2] = False   # Turning off Ulam's mode
        elif playerGuess < rand:
            print(low.format(playerGuess))
        elif playerGuess > rand:
            print(high.format(playerGuess))
    return returnList


def amILying(currentGuess):
    '''Used to check if I'm going to lie on this check, used 3
    arbitrarily to lessen the chance of lying on the first couple
    of guesses'''
    ulamRand = random.randint(currentGuess, currentGuess + 3)
    if ulamRand == currentGuess:
        return True


def main():
    # Checks if -u was passed to enable lying
    if len(sys.argv) == 2 and sys.argv[1] == "-u":
        print("Ulam's game Enabled")
        ulam = True
    else:
        print("Ulam's game Not Enabled")
        ulam = False
    rand = random.randint(1, 100)
    count = 0
    playing = True
    winning = "YOU WON in {} guesses."
    lied = ""
    # returnList is used to track if you're still playing, the number
    # of valid attemps, if ulam is in effect, and the lied message
    returnList = [True, count, ulam, lied]
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
        playing, count, ulam, lied = valInput(playerGuess, returnList, rand)
        if playing is False:    # Win Condition
            if count == 1:
                print(winning.format(count).replace("guesses", "guess"))
            else:
                print(winning.format(count))
            if lied:
                print("When I said", lied, "that was a lie")
            elif len(sys.argv) == 2:
                print("I did not lie")

if __name__ == "__main__":
    main()
