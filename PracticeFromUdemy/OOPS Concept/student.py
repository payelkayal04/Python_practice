class Student:
    #major = "CSE"

    def __init__(self, roolno, name,marks):
        self.rl = roolno
        self.name = name
        self.marks = marks

    def test(self):
        if self.marks >= 60:
            print(self.name ," has cleared the exam")
        else:
            print(self.name, "has not cleared the exam")


s1 = Student(1,"John",65)
s2 = Student(2, "Bill",45)
print(s1.marks)
print(s1.name)
s1.test()

print(s2.marks)
print(s2.name)
s2.test()