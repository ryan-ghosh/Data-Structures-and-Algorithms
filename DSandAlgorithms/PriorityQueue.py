import graph


class PriorityQueue:
    def __init__(self, capacity, list):
        self.capacity = capacity
        self.list = list

    def isFull(self):
        if len(self.list) >= self.capacity:
            return True
        else:
            return False

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def dequeueMax(self):
        if self.isEmpty():
            return "Empty"
        x = self.list.remove(max(self.list))
        return x

    def dequeueMin(self):
        if self.isEmpty():
            return "Empty"
        x = self.list.remove(min(self.list))
        return x

    def enqueue(self, item):
        if self.isFull():
            return "Capacity reached"
        self.list.append(item)

