import random

class Stack:
    def __init__(self, list: list, capacity: int):
        self.list = list
        self.capacity = capacity

    def isFull(self):
        if len(self.list) == self.capacity:
            return True
        return False

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def push(self,data):
        if self.isFull():
            print("Max capacity reached")
        else:
            self.list.append(data)

    def pop(self):
        if self.isEmpty():
            print("Empty")
        else:
            end = len(self.list)
            self.list.pop(end-1)

class Queue:
    def __init__(self, list: list, capacity: int):
        self.list = list
        self.capacity = capacity

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def isFull(self):
        length = len(self.list)
        if length == self.capacity:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isFull():
            print("Max capacity reached")
        else:
            self.list.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Empty")
        else:
            self.list.pop(0)


