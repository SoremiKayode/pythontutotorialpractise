import shutil
import os

path = os.getcwd()

# print(path)
# os.chdir(r"C:\Users\kayodebarnabas.DESKTOP-N3C038F\Downloads")
# print(os.getcwd())

# print([dir for dir in os.listdir() if dir.endswith(".txt")])

print(os.cpu_count())
print(os.name)

# print(os.get_terminal_size())

# os.makedirs("new_folder/new_document/python_document")
# # os.remove("Bose.txt")

# os.rmdir("my_file")
# os.removedirs("new_folder/new_document/python_document/my_file")
# print(os.path.exists("hello_world.py"))
print(os.stat("data_type.py"))
# os.rename("hello_world.py", "hello_coding.py")
# print(os.scandir(r"C:\Users\kayodebarnabas.DESKTOP-N3C038F\Desktop\Essencee Hairs"))
# for dirpath, dirname, filename in os.walk(r"C:\Users\kayodebarnabas.DESKTOP-N3C038F\desktop"):
#     for path, item in zip(dirpath, filename):
#         print(os.path.join(path, item))

# list1 = [1, 2, 3, 4]
# list2 = [6, 7, 8, 9]
# for item1, item2 in zip(list1, list2):
#     print(item1 * item2)

# shutil.copy2("helloworld.py", "tester.py")
# shutil.copyfile
# shutil.move("tester.py", "new_folder")

# print(shutil.disk_usage(r"C:\Users\kayodebarnabas.DESKTOP-N3C038F\Desktop\python_class"))
# path = os.getcwd()

# # shutil.make_archive("python_class", "zip", r"C:\Users\kayodebarnabas.DESKTOP-N3C038F\Desktop", path)
# shutil.unpack_archive("python_class.zip", path, "zip")
# print(os.path.join(path, "python_class.zip"))


# print(os.cpu_count())
print(dir(os.read))