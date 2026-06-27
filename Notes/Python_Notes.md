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