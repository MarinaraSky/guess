#!/usr/bin/env python
import random
import sys
import pickle


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
            returnList[2] += 1
            return returnList
    else:
        invalidInput(playerGuess)
        returnList[2] += 1
        return returnList


def invalidInput(playerGuess):
    '''Function to output invalid input string'''
    invalidOut = "\'{}\' is invalid input."
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
        if returnList[3]:   # This is checking if Ulam's game is enabled
            lying = amILying(returnList[1])  # Using the attempt number to lie
        else:
            lying = returnList[3]   # Ulam's not enabled
        if lying:
            if playerGuess < rand:
                print(high.format(playerGuess))
                returnList[4] = high.format(playerGuess).replace("is", "was")
            elif playerGuess > rand:
                print(low.format(playerGuess))
                returnList[4] = low.format(playerGuess).replace("is", "was")
            returnList[3] = False   # Turning off Ulam's mode
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


def saveStats(count, invalidCount):
    '''Function called upon winning games, used to track and print
    total game statistics'''
    games = 1
    newStats = [count, invalidCount, games]
    oldStats = [0, 0, 0]
    totalStats = []
    totalStr = "Valid Guesses: {0}\nInvalid Guesses: {1}\nGames Played: {2}"
    averageStr = "Average # of guesses: %.2f"
    try:
        file = open("stats_guess.txt", "rb")
        oldStats = pickle.load(file)    # Grabbing old stats
        file.close()
    except FileNotFoundError:   # Silently continue if file is not present
        pass
    with open("stats_guess.txt", "wb+") as file:
        for x in range(3):
            totalStats.append(newStats[x] + oldStats[x])
        pickle.dump(totalStats, file)
    average = totalStats[0] / totalStats[2]
    print("*" * 50)
    print("Running Totals")
    print(totalStr.format(*totalStats))
    print(averageStr % average)


def main():
    # Checks if -u was passed to enable lying
    ulam = False
    if "-u" in sys.argv:
        ulam = True
    rand = random.randint(1, 100)
    count = 0
    invalidCount = 0
    playing = True
    winning = "YOU WON in {} guesses."
    lied = ""
    # returnList is used to track if you're still playing, the number
    # of valid attemps, if ulam is in effect, and the lied message
    returnList = [True, count, invalidCount,  ulam, lied]
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
        playing, count, invalidCount, ulam, lied = valInput(
                playerGuess, returnList, rand
        )
        if playing is False:    # Win Condition
            if count == 1:
                print(winning.format(count).replace("guesses", "guess"))
            else:
                print(winning.format(count))
            if lied:
                print("When I said", lied, "that was a lie")
            elif "-u" in sys.argv:
                print("I did not lie")
            saveStats(count, invalidCount)
if __name__ == "__main__":
    main()
