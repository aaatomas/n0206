class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(100, 100)
rectangle2 = Rectangle(50, 50)

print(rectangle1.area(), rectangle1.perimeter())
print(rectangle2.area(), rectangle2.perimeter())
