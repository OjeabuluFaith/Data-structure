'''
3rd of november 2020

implementing QUEUE using OOP

-->ENQUEUE
-->DEQUEUE
-->size
-->is empty 


implemented using first-in first-out(FIFO)
'''


class Queue:
    def __init__(self):
        self.item = []


# check if the queue is empty

    def IsEmpty(self):
        return self.items == []

# add element  to the queue at the first spot in the queue

    def Enqueue(self, item):
        self.items.insert(0, item)

# remove element form the queue

    def Dequeue(self):
        return self.items.pop()

# confirms the size of the queue

    def Size(self):
        return len(self.items)
