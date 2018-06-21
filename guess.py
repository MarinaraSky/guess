#!/usr/bin/env python3
import random


def inputVal(check):
    '''Function used to return either the user selected integer within valid
    range or print out an error'''
    invalidOutput = "{} is invalid input"
    if check.isdigit():     # Checks if theres non numbers in string
        check = int(check)  # Converts to int object
        if (1 <= check <= 100):     # Verifies its within valid range
            return check
        else:
            print(invalidOutput.format(check))
            return False
    else:
        print(invalidOutput.format(check))
        return False


def checkInput(selection, rand):
    '''Used to check if they guess the number right and return
    high or low statement'''
    if selection == rand:
        return True
    else:
        if selection < rand:
            return print(selection, "is to low. ")
        else:
            return print(selection, "is to high. ")


def main():
    rand = random.randint(1, 100)
    guessCount = 0
    while True:     # Loop until they win
        try:
            selection = input("Please guess a number between 1 and 100: ")
        except (KeyboardInterrupt, EOFError):
            print()
            break
        selection = inputVal(selection)
        if selection:   # Wont be satisfied if check was false
            guessCount += 1     # Only increments if valid guess
            if checkInput(selection, rand):     # When right number is guessed
                print("YOU WON in ", guessCount, "guesses")
                break

if __name__ == "__main__":
    main()
