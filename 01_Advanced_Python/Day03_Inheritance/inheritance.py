class  Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} speaks")

class Dog(Animal):
        pass

d1=Dog("Tommy")
print(d1.name)

class Dog(Animal):

    def bark(self):
        print("Woof Woof")

d1=Dog("Tommy")

d1.speak()
d1.bark()

class Bird(Animal):
    def fly(self):
        print("Bird is flying")

b1=Bird("Parrot")

b1.speak()
b1.fly()

print(b1.name)

b1.fly()

b1.speak()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print("My name is ",self.name,"/nMy age is ",self.age)

p1=Person("Surya",19)

p1.introduce()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, roll_no):
        Person.__init__(self, name, age)      # Call parent constructor
        self.roll_no = roll_no

    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)      # Call parent constructor
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


# Creating Objects
s1 = Student("Surya", 19, "24SM001")
t1 = Teacher("Sharma Sir", 45, "Python")


# Calling Methods
s1.introduce()
s1.study()

print()

t1.introduce()
t1.teach()
