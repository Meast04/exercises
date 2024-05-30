from datetime import date

class Calendars:
    @property
    def today(self):
        return date.today()
    
class CalendarStub:
    def __init__(self,today):
        self.today = today
        