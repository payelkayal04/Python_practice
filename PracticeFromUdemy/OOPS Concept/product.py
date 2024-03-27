class Product:
    def __init__(self, n, des, p):
        self.name = n
        self.description = des
        self.price = p

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)


p1 = Product("Iphone", "It's awesome", 100000)
p1.display()
p2 = Product("Samsung", "It's awesome", 80000)
p2.display()
