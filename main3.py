class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width


    def _iter_(self):
        return iter([{'length': self.length}, {'width': self.width}])


rect = Rectangle(10, 5)


for dim in rect:
    print(dim)