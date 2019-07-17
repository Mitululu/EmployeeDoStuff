# Class that represents an employee of a company
# by Mitul Saha
from random import randint


class Employee:
    name = ""
    age = 0
    bdate = ""
    salary = 0
    depart = ""

    def __init__(self, name, age, bdate, salary, depart):
        self.name = name
        self.age = age
        self.bdate = bdate
        self.salary = salary
        self.depart = depart

    def info(self):
        return "The name is %s, the age is %d, the birthday is %s, the salary is %d, and " \
                "the department is %s" % (self.name, self.age, self.bdate, self.salary, self.depart)

    @property
    def serialize(self):
        return self.__dict__


def get_decodes(arr, i, len):
    curr = arr[i]

    if i+1 == len:
        return 1

    next = arr[i+1]

    if curr > 2 or (curr == 2 and next > 6 and next == 0) or curr == 0:
        return get_decodes(arr, i+1, len)
    elif next != 0:
        if i+2 == len:
            return 2
        return get_decodes(arr, i+1, len) + get_decodes(arr, i+2, len)
    else:
        return get_decodes(arr, i+2, len)


def main():
    input = [randint(1, 4)]

    for i in range(1, 8):
        if input[i-1] == 0:
            input.append(randint(1, 4))
        else:
            input.append(randint(0, 4))

    print(input)
    print(get_decodes(input, 0, len(input)))


if __name__ == "__main__":
    main()
