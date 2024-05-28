# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
import re
from abc import ABC
class Person:
    @staticmethod
    def is_valid_name(name):
        return re.fullmatch("\w+ \w+( \w+)*",name)
    def __init__(self,id,name, is_a_student):
        if not self.is_valid_name(name):
            raise ValueError
        self.id = id
        self.is_a_student = is_a_student
        self.name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if not self.is_valid_name(name):
            raise ValueError
        else : 
            self.__name = name

    
class Residence(ABC) :
    def __init__(self,address,area,number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}
    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    @property
    def maximum_occupants(self):
        return min(self.area//20, self.number_of_rooms*2)
    