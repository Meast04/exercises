class ContactsManager:
    def __init__(self):
        self.__contacts = []


    @property
    def contacts(self):
        return self.__contacts