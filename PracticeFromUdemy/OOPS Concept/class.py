class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def Average(self):
        numberOfRatings = len(self.ratings)
        averageOfRatings = sum(self.ratings) / numberOfRatings
        print("Average rating for", self.name ,"is", averageOfRatings)


c1 = Course("Java Course", [1, 2, 3, 4])
print(c1.name)
print(c1.ratings)
c1.Average()

c2 = Course("Python", [2, 2, 2, 2])
print(c2.name)
print(c2.ratings)
c2.Average()
