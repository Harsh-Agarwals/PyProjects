import random


def game():

    # ---------------HANGMAN DESIGN----------------
    hangman = {
        "1": "________\n|      |\n|\n|\n|\n|\n|_______",
        "2": "________\n|      |\n|      o\n|\n|\n|\n|_______",
        "3": "________\n|      |\n|      o\n|      |\n|\n|\n|_______",
        "4": "________\n|      |\n|      o\n|      |\n|      |\n|\n|_______",
        "5": "________\n|      |\n|      o\n|     \|\n|      |\n|\n|_______",
        "6": "________\n|      |\n|      o\n|     \|/\n|      |\n|\n|_______",
        "7": "________\n|      |\n|      o\n|     \|/\n|      |\n|     /\n|_______",
        "8": "________\n|      |\n|      o\n|     \|/\n|      |\n|     / \ \n|_______"
    }

    # ----------------HINT OPTIONS------------------
    content_properties = {
        'apple': ['Red, tennis-ball sized', 'Eating a day, keeps the doctor away!'],
        'mango': ['Yellow and Sweet', 'King of fruits'],
        'Pineapple': ['Thorny Fruit, with spike leaves', 'Grown on the soil-top'],
        'strawberry': ['Red, Sweet-sour', 'Girls fav'],
        'chocolate': ['Brown and Bitter', 'Lovers favourite'],
        'orange': ['Spherical, Sour and sweet', 'Share in pieces'],
        'banana': ['Yellow, Wrestlers food', 'Potassium rich'],
        'watermelon': ['Juicy, Red and green', "Relatable to Thompson's pudding model"],
        'guava': ['Tough and tasty, Eatable seeds', 'Parrots favourite']
    }

    # --------------CHOOSING RANDOM OPTION--------------------
    contents = list(content_properties.keys())
    chosen = random.choice(contents)
    chosenList = list(chosen.lower())
    spaces = len(chosen)
    guessList = list("_" * spaces)

    print("\nTotal chances = 8, if you finish all your chances, you will be hanged!")

    for i in guessList:
        print("_ ", end=' ')

    chances = 8
    guesses = []

    while chances > 0:
        guess = input("\nEnter your guess: ")

        if guess in guesses:
            print("\tAlready guessed!")
            print("\tPrevious guess: ", guesses)
            continue
        else:
            guesses.append(guess)
            if guess in chosenList:
                pos = [i for i in range(len(chosenList)) if chosenList[i] == guess]
                for ind in pos:
                    guessList[ind] = guess

                for i in guessList:
                    print(i, " ", end=' ')

                if guessList == chosenList:
                    print("\n\nThe word is ", chosen)
                    print("\tCONGRATULATIONS FOR YOUR WIN!")
                    cont = input("\nDO YOU WANT TO PLAY AGAIN[Y/N] ??")
                    if cont.lower() in ['y', 'yes']:
                        game()
                    else:
                        break
                else:
                    continue
            else:
                chances -= 1
                print("\tGuessed word is not in the name!")
                if chances == 0:
                    print(hangman[str(8 - chances)])
                    print("\n\nThe word is ", chosen)
                    print("\tCHANCES OVER, YOU LOOSE!")
                    cont = input("\nDO YOU WANT TO PLAY AGAIN[Y/N] ??")
                    if cont.lower() in ['y', 'yes']:
                        game()
                    else:
                        break
                elif chances > 0:
                    print(hangman[str(8 - chances)])
                    print("\n\tChances left: ", chances)
                    if chances == 3:
                        print("\n\n----------")
                        print("|  HINT  |     ", random.choice(content_properties[chosen]))
                        print("----------\n\n")

                    for i in guessList:
                        print(i, " ", end=' ')
                    print("\n\nTry Again!")


game()
