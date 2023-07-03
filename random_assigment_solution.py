import random

Guessed_names = ["Franscis", "Frank", "Fiona"]
print("Guess a name between these names")
print(Guessed_names)


a = 0
while a < 3:
    what_to_guesss = random.choice(Guessed_names)
    your_guess = input().capitalize()
    if your_guess not in Guessed_names :
        print("name not in the list, check the list carefully")
    else:
        if what_to_guesss == your_guess :
            print("You Guessed Right")
            break
        else:
            print("Guess again")
    a += 1

