number1 = 0
number_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
number_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
number_3 = 3


# while number1 < 13:
#     print(f"{number_3} * {number1} = {number_3 * number1}")
#     number1 += 1
    


def multiplication(x, y):
    while x < 13 :
        print(f"{y} * {x} = {y * x}")
        x += 1


multiplication(number1,number_3)
for x in number_list :
    multiplication(number1, x)
    print(" ")