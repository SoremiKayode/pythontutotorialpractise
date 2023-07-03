
# Condition = ""

# if Condition == "cold":
#     print("Put on a sweater")
# elif Condition == "raining":
#     print("Take an umbrealla")
# elif Condition == "hot":
#     print("wear sweat absorbant cloth")
# else:
#     print("Go out without taking anything")

a = 5
b = 10

# if a < b : print(" a is less than b")

print("Ho much Goods do you buy")
total_ammount_of_goods = int(input())

if total_ammount_of_goods < 50000 and total_ammount_of_goods >= 10000:
    print("Congratulations You won a refrigerator")
elif total_ammount_of_goods < 100000 and total_ammount_of_goods >= 50000:
    print("You've just won a laptop")
elif total_ammount_of_goods >= 100000 :
    print("You gave just won a car")
else:
    print("Sorry, Buy more to get a gift item")
