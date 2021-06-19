class Calculator:
    num = 100
    #
    # def __init__(self):
    #     print("I am called automatically")
    #     #default constructor

    def __init__(self, a, b) -> object:
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber

obj = Calculator(2,3)
obj.getData()
print(obj.num)
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.num)
print(obj1.Summation())

