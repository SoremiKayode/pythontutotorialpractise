
# # FOR LOOP
# number = 0
# number_2 = 8
# # while number < 13:
# #     print(f"{number_2} * {number} = {number_2 * number}")
# #     number += 1
# # else:
# #     print("Thank you")
# a = 0
# while a < 6 :
#     a += 1
#     if a == 3 :
#         continue
#     print(a)
student_name = ["titi", "kola", "John", "Joshua", "Jeremiah", "Felix", "Ephraim", "Festus", "Sandra"]
student_score = [70, 60, 40, 30, 100, 80, 90, 75, 55]
indexes = 0
total = 0
print(student_score[0])
for x in range(len(student_score)):
    total+= student_score[indexes]
    indexes += 1
ground_total = total

for x in student_score:
    if x < ground_total / len(student_score):
        student_position = student_score.index(x)
        name_of_student = student_name[student_position]
        print(f"{name_of_student} has failed")

