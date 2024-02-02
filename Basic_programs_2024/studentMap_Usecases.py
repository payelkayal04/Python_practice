students = {'john':['Python','Django','DRF'], 'bob':['Java','Spring'],'jim':['js','node','react']}
keys = students.keys()
for eachkey in keys:
    print("Courses taken by ",eachkey,"are")
    for eachCourse in students[eachkey]:
        print(eachCourse)