""" 
Following are the data type we have in python

text :
    category : text
    
Numeric category : 
    int numbers without decimal
    float : float are number with decimal, and it can also be scientific numbers
    complex : numbers with imaginary value

sequence type :
    list : list are collection of some items
    tuple : just like a list
    range : range(0, 2, 1)
    
mapping type :
    dictionary : it's in form of key value pairs
    
set type :
    set
    frozenset
    
booleans : boolean
    True
    False
    
binary :
    bytes, bytesarray, memoryview

"""

a = "name" # str
# you can always use type to check the data type
print(type(a))

# checking if a is a string
if type(a) == str :
    print("Yes a is a string")
    
b = 5 # This is an interger
print(type(b))
c = 2.4 # This is a float
print(type(c))
d = 2.4e-5 # This is a float
print(type(d))
e = 3j # This is a complex

#MAPPING TYPE

# This is a list
infos_of_students = ["Tola", 23, 2e6, ["frankling", "Sam"]]
print(type(infos_of_students))

# checking if the vcariabel above is a list
if type(infos_of_students) == list :
    print("Yes it is a list")
    
# This is a tuple
infos_of_workers = ("frank", 24, [1, 2, 3])
print(type(infos_of_workers))

# This is a range
matric_number = range(1, 7, 2)
print(type(matric_number))
print([x for x in matric_number])

# MAPPING TYPE
# This is a dictionary
school_database = {"studentName" : "Folakemi",
                   "studentAge" : 24}

print(school_database)
print(school_database["studentName"])

# To check the type of school_database 
print(type(school_database))

# SET TYPE 

# This is a set
student_info = {"kola", "frank", 24}
print(type(student_info))
# This is a frozen set
student_day = ({"kola", "frank", 24})
print(type(student_day))

# BOOLEANS
is_tuesday = True
is_wednesday = False

print(type(is_tuesday))
print(type(is_wednesday))

# Binary
studnet_bi = b"kayode"
print(type(studnet_bi))
print(type(bytearray(studnet_bi)))








    
