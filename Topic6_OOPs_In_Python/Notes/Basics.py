# Object-Oriented Programming (OOP) is a programming paradigm 
# that uses objects and classes 
# to structure and organize code.

# it is mandatory to pass the argument self in every
# function which is defined inside of the class


# defining the constructor

def __init__(self):
    pass

# syntax to define a class

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("Barking")


# creating object of the class dog
# and accessing methods of the class

d = Dog("Tim",5)

print(d.name)
print(d.age)
print(d.getName())

d.bark()
print(d.add_one(5))


# ------------------------


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Course:
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def printStudents(self):
        print(self.students)

if __name__ == "__main__":
    a = Student('Alice', 22)

    c = Course("Math", 5)

    c.addStudent(a)

    print(len(c.students))

    for i in c.students:
        print(i)
        print(i.name)
        print(i.age)