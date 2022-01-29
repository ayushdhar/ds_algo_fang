from typing import List


class Node:
    def __init__(self, name):
        self.children: List[Node] = []
        self.name = name
        self.visited: bool = False

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array: list):
        array.append(self.name)
        for i in self.children:
            i.depthFirstSearch(array)
        return array

    def all_children_visited(self):
        return all([i.visited for i in self.children])

    def get_next_not_visited_child(self):
        for i in self.children:
            if not i.visited:
                return i

    def depthFirstSearch(self, array: list):
        stack = []
        stack.append(self)
        array.append(self.name)
        self.visited = True
        while stack:
            top = stack[-1]

            if top.children and not top.all_children_visited():
                next_child = top.get_next_not_visited_child()
                stack.append(next_child)
                array.append(next_child.name)
                next_child.visited = True
            else:
                stack.pop()

        return array
