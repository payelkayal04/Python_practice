class Car:
    def __init__(self, make, year):
        self.year = year
        self.make = make

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine Started")


c = Car("BMW", 2017)
print(c.make)
print(c.year)
e = c.Engine(1234)
print(e.number)
e.start()