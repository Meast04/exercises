import re


class Contact:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        # self.numbers = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) & len(name) > 1 & name != None:
            self.__name = name
        else : 
            raise ValueError("Name should be a string of minimal 1 character")

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        if re.fullmatch(r'[a-z0-9.]+@[a-z0-9.]+ucll\.be', email) & email != None:
            self.__email = email

    # @property
    # def numbers(self):
    #     return self.__numbers
    
    # @numbers.setter
    # def numbers(self,numbers):
    #     pass

print(contact = Contact("kaka","maxime.leenen@gmail.be"))