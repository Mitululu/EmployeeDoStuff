# tests various applications of the employee class
# should create 10 instances of employee,
# print a list of said employees,
# print the name of the oldest employee,
# print the name of the highest salaried employee
# put the JSON code of the employee list into a txt file
# by Mitul Saha

import json
import random

from Lib.employees import Employee


def write(filepath: object, num: object) -> object:
    """

    :rtype: object
    """
    print("Starting Employee Writer")
    print("")
    empList = []
    names = ["Rodney", "Tyron", "Bobby", "Anthony", "Dwight", "Jamal", "Monroe", "Franklyn", "Raphael", "Landon",
             "Lawerence", "Marcos", "Les", "Dustin", "Jay", "Valentin", "Christopher", "Cruz", "Broderick", "Erik",
             "Verline", "Hortencia", "Margarite", "Margit", "Nicolasa", "Richelle", "Edith", "Alyson", "Casandra",
             "Sandi", "Dora", "Carin", "Carla", "Vivian", "Kacey", "Elfrieda", "Sheron", "Ignacia", "Angelyn",
             "Lavonna"]
    departs = ["HR", "IT", "Marketing", "Finance", "Comms"]

    empNum = 0
    for x in range(num):
        new = Employee(None, None, None, None, None)
        new.name = names[random.randint(0, 39)]
        new.bdate = "%d/%d" % (random.randint(1, 12), random.randint(1, 28))
        new.age = random.randint(22, 63)
        new.depart = departs[random.randint(0, 4)]
        new.salary = random.randint(40000, 150000)
        empList.append(new)

    old = empList[0]
    highPay = empList[0]

    for emp in empList:
        print(emp.info())
        if emp.age > old.age:
            old = emp
        if emp.salary > highPay.salary:
            highPay = emp

    print("")
    print("The oldest employee is %s. He/she is %d years old." % (old.name, old.age))
    print("The highest salaried employee is %s. He/she earns %d yearly." % (highPay.name, highPay.salary))

    temp_list = []
    for emp in empList:
        temp_list.append(emp.serialize)

    with open(filepath, 'w') as f:
        serialized_emp = json.dumps(temp_list)
        f.write(serialized_emp)

    print("")
    print("These employees have been written to %s in json format." % filepath)


def main():
    write("employees.json", 10)


if __name__ == '__main__':
    main()
