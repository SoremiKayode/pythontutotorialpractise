import sqlite3

print("What do you want to search")
# search = input("")
connection = sqlite3.connect("product.db")
cursor = connection.cursor()
returns = cursor.execute(f"SELECT * FROM product LIMIT 3 OFFSET 2 ")
a = 0
for record in returns:
    print(record)
    print(" ")
    print("---------------------------------------------------------")
    a+=1
print(a)
connection.commit()
connection.close()