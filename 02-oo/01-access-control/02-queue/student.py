class Queue:
    def __init__(self):
        self.queue = []
    def add(self, item):
        self.queue.append(item)
    def next(self):
        self.queue.pop(0)
    def is_empty(self):
        return self.queue == []

queue = Queue()
queue.add("Karen")
queue.add("Charle")
queue.add("Bob")
print(queue.queue)
queue.next()
print(queue.queue)
queue.next()
print(queue.queue)
queue.next()
print(queue.queue)
print(queue.is_empty())


