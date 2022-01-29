from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = deque()

        queue.append(self)

        while queue:
            elem: Node = queue.popleft()
            array.append(elem.name)
            for i in elem.children:
                queue.append(i)
        return array
