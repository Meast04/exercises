class CircularBuffer:
    def __init__(self,max_size):
        self.max_size = max_size
        self.items = []

    def add(self,item):
        self.items.append(item)
        if len(self.items) > self.max_size:
            self.items.pop(0)

    def __getitem__(self,index):
        return self.items[index]


    def __len__(self):
        return len(self.items)
