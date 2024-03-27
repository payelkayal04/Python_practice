class Employee:
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


e = Employee()
e.setId(1234)
e.setName("Payel")
print(e.getId())
print(e.getName())
