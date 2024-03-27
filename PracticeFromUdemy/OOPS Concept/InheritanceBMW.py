from abc import abstractmethod, ABC


class BMW(ABC):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stoping the car")

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self,CruiseControllEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.CruiseControllEnabled = CruiseControllEnabled

    def display(self):
        print(self.CruiseControllEnabled)

    def drive(self):
        print("Three series is being driven")


class FiveSeries(BMW):
    def __init__(self,parkingAssistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def drive(self):
        print("Five series is being driven")


b = ThreeSeries(True, "BMW", "315i" , "2018")
print(b.CruiseControllEnabled)
print(b.make)
print(b.model)
print(b.year)
b.start()
b.stop()
b.display()

f = FiveSeries(False,"BMW","515i", "2022")
f.start()
f.stop()
print(f.parkingAssistEnabled)
f.drive()

#b = BMW("BMW","B15i", "2022")

