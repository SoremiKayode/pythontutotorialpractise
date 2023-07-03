
# file = open("Bayo.txt", "r+")
# file.writelines("""
# To Forgive is divine 
# To err is human

# """)


# print(file.readline())
# # "r" -"For reading a file"
# # "w" = "write to a file"
# # "a" = "append to a file"
# # "wb" = "write an image"

# # read = read the entire file
# # readline = read the first line of the file

# file.close()
pathline = "Bose.txt"
with open(pathline, "w") as file:
    file.writelines("""
    Jeremiah is 5.5 inches
    He is so stubborn
    and h hardly do his assigment
    """)
    # print(file.read())
