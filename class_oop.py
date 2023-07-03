# from lib2to3.refactor import MultiprocessRefactoringTool
import random
import sqlite3
# oop - object oriented programming 

# Car : 

# PARAMETERS 
# Wheel 
# Chair
# Door 
# Bumper 
# Flood light 
# Radio 
# engine  

# METHOD - FUNCTIONALITIES
# Move forward 
# move bacward 
# play music 
# it can convey people 
# it convey Goods 
class Car :
    """
    This is an object that tells a car how to move
    This car take some parameters :
    mode : the model name of the car
    mandate : the manufacturing date of the car

    """
    def __init__(self, model : str, mandate : int ) :
        self.name = model 
        self.date = mandate



    wheel = 4
    chair = 2
    door = 2
    bumper = 2
    flood_light = 4
    Radio = 1
    engine = 1

    def mand(self):
        """This is dsiplaying the manufacturing date of the car"""
        print(f"The name of this car is {self.name}")
    def move_forward(self):
        print("mOve forward")
    def move_backward(self):
        print("mOve forward")
    def play_music(self):
        print("mOve forward")
    def convey_people(self):
        print("mOve forward")
    def convey_goods(self):
        print("mOve forward")

# x = Car("Lambourghini", 2015)x = Car("Lambourghini", 2015)

class Engine(Car):
    def __init__(self, model, mandate):
        Car.__init__(self, model, mandate)
        print("I am a children")

    def mandate(self):
        print("The manufacturing date is 2010")
        
# single inheritance
c = Engine("Lambourghini", 2015)

print(c.flood_light)
print(c.move_forward())
print(c.mandate())