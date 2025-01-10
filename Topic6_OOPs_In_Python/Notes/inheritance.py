class Animal :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name)
        print(self.age)

    def meow(self):
        print("I don't know what to say")

    def bark(self):
        print("I don't know what to say")

class Cat(Animal):
    def meow(self):
        print("Meow")

class Dog(Animal):
    def bark(self):
        print("Barking")

if __name__ == "__main__":
    c = Cat("cat", "5")
    d = Dog("dog",7)

    # c.show()
    # d.show()

    a = Animal("A", 10)

    # function overriding

    a.meow()
    a.bark()
    c.meow()
    d.bark()
    

    # -------------------------

    class Parent:
        def __init__(self, age, name):
            self.name = name
            self.age = age

    class Child:
        def __init__(self, age, name, colour):
            super().__init__(age,name)
            self.colour = colour