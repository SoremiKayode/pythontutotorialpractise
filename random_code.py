import random
# print(random.random())
# print(random.randrange(1, 5, 3))
a = [1, 2, 3, 4]
# print(random.choice(a))
# print(random.choices(a, k=2))

# # print(random.randint(1, 10))
# random.shuffle(a)
# print(a)

random_numbers = random.randrange(1, 5)
count = 0
while count < 5:
    print("Guess any number between one and Five")
    guessed_number = int(input())

    if random_numbers == guessed_number :
        print("You Guessed right")
        break
    else:
        print("Guessed number was wrong")
        print("Guess again")
    if count == 5 :
        print("Game over, you have exceeded your guess limit")
    count+=1