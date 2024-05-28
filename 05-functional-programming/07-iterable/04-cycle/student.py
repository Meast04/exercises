class Cycle:
    def __init__(self,value):
        self.__value = list(value)
        self.__index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index = (self.__index + 1) % len(self.__value)
        return self.__value[self.__index]