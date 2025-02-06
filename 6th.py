class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'

    def __repr__(self):
        return f'{self.brand!r} {self.model!r} {self.year!r}'


car1 = Car('BMW', "i520", 2019)
car2 = Car('VW', "Tiguan", 2020)

print("STR: " + str(car1))
print("REPR: " + repr(car1))