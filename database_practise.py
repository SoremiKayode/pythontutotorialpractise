import sqlite3

conn = sqlite3.connect("school_info.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS student_info(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(200), age INTEGER, dob TEXT) ")
cursor.execute("CREATE TABLE IF NOT EXISTS exam_score(id INTEGER PRIMARY KEY AUTOINCREMENT, subject VARCHAR(200), score INTEGER) ")

# cursor.execute("""
# INSERT INTO student_info(name, age, dob) VALUES ('Jeremiah Olasoji', 12, 2000)
# """)
# cursor.execute("""
# INSERT INTO student_info(name, age, dob) VALUES ('Joshua Olasoji', 14, 2008)
# """)
# cursor.execute("UPDATE student_info SET name = 'Chidera', age = 23 WHERE id = 1")
cursor.execute("DELETE FROM student_info WHERE id = 1")
details = cursor.execute("""
SELECT * from student_info
""")

for x in details :
    print(x)
conn.commit()
conn.close()

