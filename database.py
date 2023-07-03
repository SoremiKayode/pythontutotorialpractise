# from ast import Delete
# from msilib.schema import CreateFolder
# from turtle import update


# CRUD - 
# C = Create 
# R = Read 
# U = update 
# D = Delete




# create a connection
# create a cursor 
# commit the cursor 
# close the connection

# string type = TEXT, VARCHAR, CHAR 
# Number = INTERGER, FLOAT, 
# BOOL = 

import sqlite3

Name = input("What is our Name?  eg. Soremi Kayode  ")
Email = input("What's your email?  ")
Adr = input("What is our Address?  ")
Age = input("What is our Age?  ")
State = input("What is your state of origin?  ")
Dob = input("What is your dob?  ")
Health = input("What is your health status?")


connection = sqlite3.connect("Student_Database.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE if not exists student_details(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email VARCHAR(200) UNIQUE, address TEXT, age INTEGER, state_of_origin TEXT, dob TEXT, health_status TEXT)")
a = 0
# while a < 20:
if "@" in Email:
    cursor.execute("""INSERT INTO student_details(name, email, address, age, state_of_origin, dob, health_status)
    VALUES(?, ?, ?, ?, ?, ?, ?)""", (Name, Email, Adr, int(Age), State, Dob, Health))
else:
    print("Email format is incorrect")


#     a += 1
# details = cursor.execute("SELECT * FROM student_details")
# for detail in details:
#     print("Id: ", detail[0])
#     print("Name: ", detail[1])
#     print("Email: ", detail[2])
#     print("Address: ", detail[3])
#     print("Age: ", detail[4])
#     print("State of Origin: ", detail[5])
#     print("Date of birth: ", detail[6])
#     print(" ")
# cursor.execute("UPDATE student_details SET name = 'Josep Fams' where id = 1")
# to edit a row in a database use this instructions; UPDATE then folowed by the table name, then SET
# folowed by name of the column you want to change one of it's data, followed by the value you want to change to
# followed by the word WHERE, foloowed by the column key
# cursor.execute("UPDATE student_details SET name = 'Josep Fams' where id = 2")
# cursor.execute("DELETE student_details WHERE id = 1")
# informations = cursor.execute("SELECT name, email, address, age FROM student_details WHERE name = 'Sandra Stone_14'")

# for info in informations:
#     print(info)

connection.commit()

connection.close()



