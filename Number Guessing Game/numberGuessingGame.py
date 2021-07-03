import numpy as np

num = np.random.randint(1, 100)

print("A random number is chosen between 1 and 100. You are given 10 chances to find the correct number.\nBEST OF LUCK\n")

chances = 10
guesses = []


def checkGuess(guess, num):
    return guess == num


while chances > 0:
    guess = int(input("Enter your guess: "))
    guesses.append(guess)
    chances -= 1
    if checkGuess(guess, num):
        print("CONGRATULATIONS, YOUR GUESS IS CORRECT\n\tYOU WIN THE GAME!")
        break
    else:
        if guess > num:
            print("\tGuess is too high.")
            print("\tAll guesses: ", guesses)
            if chances == 0:
                print("CHANCES OVER, YOU LOOSE!\nPLAY ANOTHER GAME")
            elif chances > 0:
                print("\tChoose another number!\n\tChances left: ", chances)
        else:
            print("\tGuess is too low.")
            print("\tAll guesses: ", guesses)
            if chances == 0:
                print("CHANCES OVER, YOU LOOSE!\nPLAY ANOTHER GAME")
            elif chances > 0:
                print("\tChoose another number!\n\tChances left: ", chances)
