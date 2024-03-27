class Programmer1:
    def setName(self,n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self,techs):
        self.technologies = techs

    def getTechnologies(self):
        return self.technologies


p1 = Programmer1()
p1.setName("John")
p1.setSalary(1000)
p1.setTechnologies(["Java", "C", "C++", "Python"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())