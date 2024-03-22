class Money:
    def __init__(self,currency):
        self.value = 0
        self.currency = currency

    def __add__(self):
        if self