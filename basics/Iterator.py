fruits = ["apple", "banana", "mango"]
fruits_iter = iter(fruits)
print(next(fruits_iter))
print(next(fruits_iter))


class UniqueNumberIterator:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        if self.x >= 4:
            raise StopIteration
        self.x += 1
        return self.x


number = UniqueNumberIterator(0)
print(next(number))
print(next(number))
