class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        self.ds = []

    def buildHeap(self, array):
        for i in array:
            self.insert(i)
        return self.ds

    def siftDown(self):
        # Write your code here.
        pass

    def siftUp(self):
        # Write your code here.
        pass

    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        # Write your code here.
        pass

    def insert(self, value):
        # Write your code here.
        pass
