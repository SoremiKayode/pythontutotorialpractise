# time = "morning"
# def prepare_food(time_of_day):
#     if time_of_day == "morning":
#         print("Robot Please make conflakes for me")
#     elif time_of_day == "afternoon":
#         print("Robot Please prepare sand witches for me ")
#     elif time_of_day == "evening":
#         print("Robot Please prepare Semo for me")
#     else:
#         print("Wait till above stated time is fufilled")

# prepare_food(time)
# prepare_food("afternoon")
# prepare_food("evening")



# # def good_morning(name, secondname):
# #     print(f" Good morning {name[1]}")
# #     print(f" Good morning {secondname}")

# # good_morning("Jeremiah", "Joshua")

# def census(*args):
#     for family_member in args:
#         print(family_member)

# census("Sandra", "Felix", "Jeremiah")
# census("Felix", "Jeremiah")

# # def greet():
# #     pass

# # greet()
student_details = {
"name" : ["Jeremiah", "Joshua", "John", "Felix", "Yomi", "Shola"],
"age" : ["30", "26", "12", "15", "23", "17"],
"height" : ["18-05-1992", "13-1-1998", "10-5-2010", "12-06-2007", "25-07-1999", "13-08-2005"],
}
# print(student_details["name"][0])
def connect_database(**kwargs):
    """"
    keyword : 
    name : must be name of person in the database, name must be lower case
    age :  must be age of person in the database
    
    """
    if "name" in kwargs:
        index = student_details["name"].index(kwargs["name"])
        file = open(student_details["name"][index], "w")
        file.write(student_details["name"][index])
        
        # print(student_details["name"][index])
        # print(student_details["age"][index])
        # print(student_details["height"][index])

connect_database(age = "30")

# x = lambda a : a * 10

# print(x(10))

def x():
    return 10

print(x())