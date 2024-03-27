n = int(input("Enter the number of employees : "))
employees = {}
for i in range(n):
    name = input("Enter the name of the employee: ")
    salary = int(input("Enter the salary of the employee: "))
    employees[name] = salary
while True:
    name = input("Enter the name of the employee: ")
    salary = employees.get(name, -1)
    if salary == -1:
        print("Employee doesn't exist")
    else:
        print("The salary of this employee is :",salary)
    choice = input("Do you want to know the salary of another employee:[Yes|No] ")
    if choice.lower() == 'no':
        break
    else:
        print("Make a correct choice: ")

