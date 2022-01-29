class Stack:

    def __init__(self):
        self.data = []

    @property
    def top(self):
        if not self.is_empty:
            return self.data[-1]
        return -1

    @property
    def is_empty(self):
        return not self.data

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if not self.is_empty:
            return self.data.pop()
        return -1


def is_balanced(s: str):
    helper = Stack()

    for i in s:
        if i == "(":
            helper.push(i)
        elif i == ")":
            if helper.top == "(":
                helper.pop()
            else:
                return False
    return len(helper.data) == 0


a = None
b = None

print((a is None) ^ (b is None))
