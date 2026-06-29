# Python Notes

## Day 1 - Classes and Objects

### What is a Class?

A class is a blueprint for creating objects.

Example:

```python
class Student:
    pass
```

---

### What is an Object?

An object is an instance of a class.

Example:

```python
student1 = Student()
```

---

### Class Attributes

Attributes store information inside a class.

Example:

```python
class Student:
    college = "IIITDM Jabalpur"
```

---

### Key Learnings

- Learned what OOP is.
- Understood the difference between a class and an object.
- Created multiple objects.
- Accessed class attributes.

---

### Doubts

- Why do two objects show the same class attribute?
- What does `<__main__.Student object at ...>` mean?

# Day 2 - Constructors and Methods

## What I Learned

### Constructor
- Constructor is a special method in Python.
- It is automatically called when an object is created.
- The constructor is written as `__init__()`.

Syntax:
```python
class Student:
    def __init__(self):
        print("Constructor called")
```

---

### self

- `self` refers to the current object.
- It is used to access attributes and methods of the object.
- Every instance has its own values stored using `self`.

Example:

```python
self.name = name
```

---

### Instance Attributes

Attributes belong to an object.

Example:

```python
self.name
self.age
self.salary
```

Different objects can have different values.

---

### Methods

Methods are functions defined inside a class.

Example:

```python
def show_details(self):
    print(self.name)
```

Methods define the behavior of an object.

---

## Difference

Attribute → Stores data

Method → Performs an action using the data

---

## Real-world Analogy

Class → Blueprint

Object → Actual product

Constructor → Initializes the object

Attributes → Properties

Methods → Actions

---

## Mini Projects Completed

- Student
- Laptop
- Car
- Employee

---

## Interview Question

Q. Why do we use constructors?

Answer:
Constructors automatically initialize object data when an object is created, making code cleaner and avoiding manual assignment.

---

## Today's Learning

Today I learned how Python objects store their own data using constructors and how methods define the behavior of those objects.

📘 Day 3 Notes - Inheritance in Python
What is Inheritance?

Inheritance is an OOP concept in which one class acquires the properties (attributes) and behaviors (methods) of another class.

It promotes:

Code Reusability
Better Organization
Easier Maintenance
Terminology
Parent Class (Base Class)

The class whose properties are inherited.

Example:

class Animal:
    pass
Child Class (Derived Class)

The class that inherits from another class.

Example:

class Bird(Animal):
    pass

Here,

Animal → Parent Class
Bird → Child Class
Syntax
class Parent:
    pass

class Child(Parent):
    pass

The child class automatically gets access to all public attributes and methods of the parent class.

Example
class Animal:
    def speak(self):
        print("Animal speaks")

class Bird(Animal):
    def fly(self):
        print("Bird is flying")

b1 = Bird()

b1.speak()
b1.fly()

Output

Animal speaks
Bird is flying
Why Use Inheritance?

Without inheritance:

class Bird:
    def speak(self):
        print("Animal speaks")

    def fly(self):
        print("Bird is flying")

Every animal class would need its own speak() method.

With inheritance:

Animal
   ↑
Bird
Dog
Cat
Horse

Only write speak() once.

Constructor Inheritance

If the child class doesn't have its own constructor, it automatically uses the parent's constructor.

Example:

class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    pass

b1 = Bird("Parrot")

print(b1.name)

Output

Parrot
Adding New Methods

A child class can have its own methods.

Example:

class Animal:
    def speak(self):
        print("Animal speaks")

class Bird(Animal):
    def fly(self):
        print("Bird flies")

Bird now has:

speak()
fly()
Important Points

✅ Child class inherits attributes.

✅ Child class inherits methods.

✅ Parent class cannot access child class methods.

Example:

a = Animal()

a.fly()

This gives an error because fly() belongs only to Bird.

Real Life Examples
Vehicle
Vehicle
│
├── Car
├── Bike
├── Bus

Vehicle has:

start()
stop()

Car additionally has:

openSunroof()

Bike additionally has:

wheelie()
Employee
Employee
│
├── Teacher
├── Manager
├── Engineer

Employee:

name
salary

Teacher:

subject

Engineer:

programming_language
Advantages

✔ Code Reusability

✔ Less Code Duplication

✔ Easier Maintenance

✔ Better Code Organization

✔ Extensibility

Disadvantages

❌ Can create complex class hierarchies.

❌ Deep inheritance makes debugging difficult.

Interview Questions
Q1. What is inheritance?

Inheritance is the process through which one class acquires the properties and methods of another class.

Q2. Why do we use inheritance?

To reuse existing code and avoid duplication.

Q3. Which class is inherited?

The Parent (Base) class.

Q4. Which class inherits?

The Child (Derived) class.

Q5. Can a parent class access child methods?

No.

Q6. Can a child class access parent methods?

Yes.

Key Takeaways
Inheritance allows one class to reuse another class's code.
The parent class provides common functionality.
The child class can add its own functionality while still using the parent's features.
It is one of the four pillars of Object-Oriented Programming (OOP).


📘 Day 4 Notes – Polymorphism & Method Overriding
1. What is Polymorphism?

Definition:
Polymorphism means "one interface, many forms."

Poly = Many
Morphism = Forms

In Python, polymorphism allows the same method name to perform different actions depending on the object that calls it.

Example
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

Dog().speak()
Cat().speak()

Output

Bark
Meow

Although both classes have the same method name (speak()), the behavior is different.

2. What is Method Overriding?

Definition:

Method overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

Example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

Here, Dog overrides the speak() method of Animal.

3. How Python Searches for Methods

When we call

dog.speak()

Python checks in this order:

Child Class
      ↓
Method Found?
      ↓
Yes → Execute it

No
      ↓
Parent Class
      ↓
Method Found?
      ↓
Yes → Execute it

No
      ↓
AttributeError
4. What is Runtime Polymorphism?

The method that gets executed is decided while the program is running, based on the actual object.

Example:

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()

Output

Bark
Meow
Moo

The loop simply calls:

animal.speak()

Python automatically selects the correct method.

5. Why Do We Use Polymorphism?

✅ Reduces if-else statements.

✅ Makes code flexible.

✅ Makes programs easier to extend.

✅ Improves code readability.

✅ Used in large software projects and frameworks.

6. Difference Between Inheritance and Polymorphism
Inheritance	Polymorphism
Child inherits from parent	Same method behaves differently
Creates relationship	Provides different behavior
Used for code reuse	Used for flexibility
7. Method Overriding vs Method Overloading
Method Overriding
class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        print("Dog")

✔ Supported in Python.

Method Overloading
def add(a, b):
    pass

def add(a, b, c):
    pass

❌ Python does not support traditional method overloading. The second definition replaces the first. (There are alternative techniques, but this classic form doesn't work.)

8. Calling Parent's Method

Use super().

Example

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

Output

Animal speaks
Dog barks

super() calls the parent class's method.

9. Using pass

Example

class Employee:
    def work(self):
        pass

pass means:

"Do nothing for now."

The child class will implement the method.

10. Better Practice

Instead of

pass

Use

raise NotImplementedError("Subclasses must implement work()")

This forces every child class to define its own version of the method.

11. Real-Life Example
class Payment:
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class Card(Payment):
    def pay(self):
        print("Paid using Card")

class Cash(Payment):
    def pay(self):
        print("Paid using Cash")

payments = [UPI(), Card(), Cash()]

for payment in payments:
    payment.pay()

Output

Paid using UPI
Paid using Card
Paid using Cash

This is a practical example of polymorphism.

⭐ Interview Definitions
Polymorphism

Polymorphism is the ability of the same method or interface to perform different actions depending on the object that invokes it.

Method Overriding

Method overriding is when a child class provides its own implementation of a method that is already defined in its parent class.

🧠 Key Takeaways
✔ Polymorphism means one interface, many forms.
✔ Method overriding is the most common way to achieve polymorphism in Python.
✔ Python first looks for a method in the child class, then in the parent class.
✔ super() is used to call the parent class's method.
✔ pass is a placeholder; NotImplementedError is better when a method must be implemented by subclasses.
✔ Polymorphism makes code more flexible, reusable, and maintainable.