student = ["Kola", "Tayo", "Felix", 24, 3j]
# student_2 = ("John", "Jeremiah", "Joseph")
student_2 = ["Kola", "John", "Jeremiah", "Joseph"]
number = [1, 3, 4, 2, 4, 6, 3, 4, 6, 5, 7, 10, 1, 2, 3]
number_2 = [i for i in number if i < 5]
# print(number_2)
odd = []

for i in student:
    if i not in student_2:
        odd.append(i)

print(odd)
# print(student[-2])
# print(student[:3])
# print(student[-4:-1])

# if "John" in student:
#     print("Yes Tayo is in student")
# else:
#     print("not in student")

# student[1] = "John"
# student[:2] = ["John", "Joseph", "Jeremiah"]
# student.append("Joseph")
# student.insert(1, "Jeremiah")
# student.extend(student_2)
# student.remove("Felix")
# student.pop()
# student.pop(2)
# del student[1]
# del student
# student.clear()

# print(student)
# for i in student:
#     print(i)

# print(len(student))
# for i in range(len(student)):
#     print(student[i])
# x = 0
# while x < len(student) - 2 :
#     print(student[x])
#     x += 1

import random
print(random.choice())
