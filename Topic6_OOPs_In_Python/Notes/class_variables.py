
class Person:
    # class variable
    number_of_people = 0

    def __init__(self, name):
        self.name = name

    # class method

    @classmethod
    def increment(cls):
        return cls.number_of_people

p1 = Person("tim")
p2 = Person("jill")

Person.number_of_people = 8
print(Person.number_of_people)