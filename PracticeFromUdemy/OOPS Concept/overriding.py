class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stoping the car")


class ThreeSeries(BMW):
    def __init__(self, CruiseControllEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.CruiseControllEnabled = CruiseControllEnabled

    def display(self):
        print(self.CruiseControllEnabled)

    def start(self):
        print("Remote start")


t = ThreeSeries(True, "BMW","325i", "2018")
print(t.make)
print(t.model)
print(t.year)
t.start()

