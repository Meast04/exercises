# Write your code here
class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds 

    @property
    def hours(self):
        return self.__hours
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self,hours):
        if 0 <= hours <= 23:
            self.__hours = hours
        else : 
            raise ValueError
        
    @minutes.setter
    def minutes(self,minutes):
        if 0 <= minutes <= 59:
            self.__minutes = minutes
        else : 
            raise ValueError
    @seconds.setter
    def seconds(self,seconds):
        if 0 <= seconds <= 59:
            self.__seconds = seconds
        else : 
            raise ValueError
        
        
        


    
