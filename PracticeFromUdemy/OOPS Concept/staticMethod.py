class objectCounter:

    numberOfObjects = 0

    def __init__(self):
        objectCounter.numberOfObjects += 1

    @staticmethod
    def DisplayCount():
        print(objectCounter.numberOfObjects)

o1 = objectCounter()
o2 = objectCounter()
o3 = objectCounter()
o4 = objectCounter()
objectCounter.DisplayCount()