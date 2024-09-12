#Topic: Custom Classes in Python


#When iterated, it first returns the length in the correct format, followed by the width.
class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width


    def _iter_(self):
        return iter([{'length': self.length}, {'width': self.width}])


rect = Rectangle(10, 5)


for dim in rect:
    print(dim)
