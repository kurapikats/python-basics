class Student:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def inputData(self):
        print("Accepting Data")
        self.name = input("Type name: ")
        self.contact = input("Type contact number: ")

    def showData(self):
        print("The name is: " + self.name + ", Contact #: " + self.contact)


class ScienceStudent(Student):
    def __init__(self, age):
        self.age = age

    def showAge(self):
        print(self.age)


newSciStudent1 = ScienceStudent(35)
newSciStudent1.inputData()
newSciStudent1.showData()
newSciStudent1.showAge()
