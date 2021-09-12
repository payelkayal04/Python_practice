from datetime import date


def calculate_Age(birthDate):
    today = date.today()
    boolean_condition = ((today.month, today.day) < (birthDate.month, birthDate.day))
    print(boolean_condition)
    print(today.month)
    print(today.day)
    print(birthDate.month)
    print(birthDate.day)
    age = today.year - birthDate.year - boolean_condition
    return age
    #print(today)


print(calculate_Age(date(1993, 9, 2)), "years")