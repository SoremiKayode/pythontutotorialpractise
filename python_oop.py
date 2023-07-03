# my_name = "Joseph"
# name = "John"

# def stand_up(name):
#     print(f"{name} Stand up")

# def sit_down(name):
#     print(f"{name} Sit down")

# def eat(name):
#     print(f"{name} Eat")

# def sleep(name):
#     print(f"{name} Go and sleep")

# def shout(name):
#     print(f"{name} Shout")

# oop -  object oriented programming, it's a style of programming that tend tend to write code that mimick an object
import random
class laptop():
    ram = "200Gb"
    def __init__(self, laptop_name, year_of_manufacturing, supported_os):
        self.laptop_name = laptop_name
        self.year_of_manufacturing = year_of_manufacturing
        self.supported_os = supported_os
        
    def boot(self, time:str, **kwargs):
        """This method defines the fact that a laptop can boo
          time : time simply how long it will take the laptop to boot - it has to be string
          """
        if "speed" in kwargs:
            print(kwargs["speed"])

        print("I am booting ", self.supported_os)
        print(f"It's going to take {time} to boot")
    

class laptop_2(laptop):
    def __init__(self, laptop_name, year_of_manufacturing, supported_os,  prod_year):
        super().__init__(laptop_name, year_of_manufacturing, supported_os)
        self.prod_year = prod_year


device = laptop_2("2005", "Dell", "2009", "mac")
device.boot("2 minute", speed = 3)