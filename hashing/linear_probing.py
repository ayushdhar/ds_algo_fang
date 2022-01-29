class LinearProbingHash:
    @staticmethod
    def __hash_function(value: int, i: int):
        return ((value % 10) + i) % 10

    def __init__(self, n):
        self.ds = [None for _ in range(2 * n)]
        self.loading_factor = sum(filter(None, self.ds)) / (2 * n)

    def insert(self, value):
        if self.loading_factor <= 0.5:
            added = False
            i = 0
            while not added:
                index = self.__hash_function(value=value, i=i)
                if not self.ds[index]:
                    self.ds[index] = value
                    added = True
                else:
                    i += 1
        else:
            print("hash ds full")

    def search(self, value):
        i = 0
        while True:
            index = self.__hash_function(value=value, i=i)
            if self.ds[index] == value:
                return index
            elif not self.ds[index]:
                return -1
            else:
                i += 1


lph = LinearProbingHash(7)
insert_array = [26, 30, 45, 23, 25, 43, 74]

for i in insert_array:
    lph.insert(i)

print(lph.search(75))
