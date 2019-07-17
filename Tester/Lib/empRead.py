# reads a JSON text file of an Employee list,
# prints the Employee values within the file
# if there's no such file, print that status
# by Mitul Saha

import sys
import json

from Lib.employees import Employee


def read(filepath):
    print("Checking the file %s for JSON Employee types" % filepath)
    print("")

    with open(filepath, "r") as f:
        jList = json.load(f)

    print("Found a json list; contents follow")
    print(jList)
    print("")

    empList = []
    for jEmp in jList:
        temp = Employee(None, None, None, None, None)
        temp.name = jEmp["name"]
        temp.age = jEmp["age"]
        temp.bdate = jEmp["bdate"]
        temp.salary = jEmp["salary"]
        temp.depart = jEmp["depart"]
        empList.append(temp)

    print("Descriptions of the employees follow")
    for emp in empList:
        print(emp.info())


def main():
    args = sys.argv
    jsonfile = ""
    tag = ".json"

    for arg in args:
        if arg.endswith(tag):
            jsonfile = arg

    if jsonfile == "":
        print("no json file argument found")
        exit(0)

    read(jsonfile)


if __name__ == '__main__':
    main()
