# Python Synstax
# a-12  = 12


import pickle
from typing import Mapping

b = 15

# rule :
# a variable can only contain letters, numbers and underscore number 
# variable cannot start with a number
# variable cannot contain a space letter
# variable with more than one name cannot be seperated with hyphen

# camelCase number 

josephAge = 10

# snake case 
joseph_age = 10

# Pascal case
JosephAge = 10

# Data Type ;
# Boolean = True
# Number = 44
# Binary = 66666
# mapping = {
#     "name" : "John Samuel",
#     "ages" : [1, 2, 3, 4, 5, 6]
# }
# Set = {1, 2, 3, 4, 5} 
# FrozenSet = ({1, 2, 3, 4, 4})
# String = "Today is Good"
# list : [1, 2, 3, 4]

# name = "Andrew Frank"
# school_lecture = "Crown Lake"
# age = 55
# favourite_food = "Fried Plantain and Rice"
# subject_taught = "French and foreing Language"
# college_attended = "Colorado university"
# children_name = "kids, Kate, Florence and Sam"

# comprehension1 = f"""
# Mr {name} is the fairest teacher in my school. {school_lecture}
# He is {age} Years
# His best food is {favourite_food}
# He teaches {subject_taught}
# Mr {name} has three kids, {children_name}
# He attend {college_attended}
# """
# comprehension2 = f"""
# Mr {name} is the fairest teacher in my school. {school_lecture}
# He is {age} Years
# His best food is {favourite_food}
# He teaches {subject_taught}
# Mr {name} has three kids, {children_name}
# He attend {college_attended}
# """
# comprehension3 = f"""
# Mr {name}is the fairest teacher in my school. {school_lecture}
# He is {age} Years
# His best food is {favourite_food}
# He teaches {subject_taught}
# Mr {name} has three kids, {children_name}
# He attend {college_attended}
# """
# comprehension4 = f"""
# Mr {name}is the fairest teacher in my school. {school_lecture}
# He is {age} Years
# His best food is {favourite_food}
# He teaches {subject_taught}
# Mr {name} has three kids, {children_name}
# He attend {college_attended}
# """
# comprehension5 = f"""
# Mr {name}is the fairest teacher in my school. {school_lecture}
# He is {age} Years
# His best food is {favourite_food}
# He teaches {subject_taught}
# Mr {name} has three kids, {children_name}
# He attend {college_attended}
# """
# comprehension6 = f"""
# Mr {name}is the fairest teacher in my school. {school_lecture}
# He is {age} Years
# His best food is {favourite_food}
# He teaches {subject_taught}
# Mr {name} has three kids, {children_name}
# He attend {college_attended}
# """
# print(comprehension1)
# print(comprehension2)
# print(comprehension3)
# print(comprehension4)
# print(comprehension5)

name_of_student = "Jeremiah", "Joseph", "Joshua", "Dara"
file = folder = director = "Myschool Result"
avg_test, *exam_score = 16, 16, 10, 40

# print(name_of_student)
# print(file)
# print(director)
# print(folder)
# print(avg_test)
# print(exam_score)
name = "Jeremiah" # string 
age = 10 # int
height = 3.4 #float
friend = ["Bola", "Kemi"] # list
last_score = (20, 30, 40, 50) #tuple
height_variation = {2.4, 4.5, 6.5} #set
com = 4j #complex
school_profile = {
    "name" : ["Kola", "Frank"],
    age : [24, 20]

}
bin = [0, 0, 0, 0, 1, 1, 1, 1]

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(friend))
# print(type(last_score))
# print(type(height_variation))
# print(type(True))
# print(type(4j))
# print(type(school_profile))
# print(type(bin))
# print(sum(bin) / len(bin))
# file = open("exam.txt", "r+")
# print(file.read())
# file.write("Hello world")
# print(file.read())
# file.close()

# with open("text_icon.png", "rb") as f:
#     print(type(f.read()))

# with open("text_icon.png", "rb") as f:
#     file = f.read()
#     print(type(file))

# string 
# Number : int, float and complex 
# sequence type : list, tuple, range
# set type : set, frozenset
# boolean : True | False 
# binary : bytes bin()
# Mapping : Dictionary

# print(range(12))
# for a in range(10):
#     print(a)
# a = {1, 2, 3}
# b = ({1, 2, 3, 4})

# for olodo in b:
#     print(olodo)

# d = {
#     "name" : "John",
#     "age" : [23, 4, 5, 6, 7]

# }

name = "Todia is Great"
comp = """
Ben is Years
His best food is {favourite_food}
He teaches {subject_taught}
Mr {name} has three kids, {children_name}
He attend Country Home college
"""

# print(comp.lower())
# print(comp.capitalize())
# print(comp.upper())
# print("la" in comp)
# print("la" not in comp)
print(name.endswith("Great"))



