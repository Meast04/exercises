from datetime import date


class Task:
    def __init__(self,description,due_date):
        self.__description = description
        self.__due_date = due_date
        self.finished = False

    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    

class TaskList:
    def __init__(self,calendar):
        self.__tasks = []
        self.__calendar = calendar

    def add_task(self,task):
        if task.due_date < self.__calendar.today:
            raise RuntimeError
        else:
            self.__tasks.append(task)

    def __len__(self):
        return len(self.__tasks)
    
    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished == True]

    @property
    def due_tasks(self):
        return [task for task in self.__tasks if not task.finished]      

    @property 
    def overdue_task(self):
        return [task for task in self.__tasks if not task.finished and task.due_date < self.__calendar.today]  

