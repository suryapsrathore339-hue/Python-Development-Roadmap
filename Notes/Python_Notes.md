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

Day 5 Notes – Encapsulation


1. What is Encapsulation?

Definition:

Encapsulation is the process of binding data (variables) and methods (functions) together inside a class while restricting direct access to the data.

It helps in:

Data Hiding
Data Protection
Controlled Access
2. Why do we need Encapsulation?

Suppose we have

class BankAccount:
    def __init__(self):
        self.balance = 1000

Anyone can do

account.balance = -100000

Problems:

Invalid balance
No security
Object loses control over its own data

Instead

account.deposit(500)

account.withdraw(200)

The object itself decides whether the operation is valid.

3. Access Specifiers in Python
Public
self.name

Accessible from anywhere.

Example

student.name
Protected
self._name

Single underscore.

Means:

"Please don't access directly."

It is only a convention.

Private
self.__balance

Double underscore.

Cannot be accessed directly.

Python performs Name Mangling.

4. Name Mangling

Example

class Student:
    def __init__(self):
        self.__marks = 95

Trying

student.__marks

gives

AttributeError

Internally Python stores it as

student._Student__marks

Purpose:

Avoid accidental access.
Prevent accidental overriding in subclasses.

Important: Name mangling is not absolute security. It is meant to discourage direct access.

5. Private Variables

Declaration

self.__balance

Access only through methods like

deposit()

withdraw()

display_balance()
6. Input Validation

Never trust user input.

Example

deposit(-500)

Wrong.

Correct

if amount > 0:

Similarly

withdraw(-100)

should not be allowed.

7. Business Logic

A software engineer thinks about rules before writing code.

For Bank Account

Deposit rules

Amount > 0

Withdraw rules

Amount > 0
Amount <= Current Balance

These rules are called Business Logic.

8. Edge Cases

Edge cases are situations that programmers often forget.

Example

Balance = 1000

Withdraw

1000

Should it be allowed?

Yes.

Hence

amount <= balance

instead of

amount < balance

Another edge case

withdraw(-500)

Without validation

balance -= (-500)

Balance increases.

9. deposit() Method

Logic

if amount > 0:
    self.__balance += amount

Otherwise

print("Invalid Input")
10. withdraw() Method

Logic

if amount > 0 and amount <= self.__balance:
    self.__balance -= amount
else:
    print("Invalid Input")

Professional version

if amount <= 0:
    print("Invalid Amount")

elif amount > self.__balance:
    print("Insufficient Balance")

else:
    self.__balance -= amount
11. Display Method

Good version

def display_balance(self):
    print("Account Holder :", self.name)
    print("Current Balance :", self.__balance)
12. super()

Today we revised

super().method()

It calls the parent class's method, not always the constructor.

Examples

super().__init__()

Parent constructor.

super().display()

Parent display method.

13. Method Overriding

Parent

show()

Child

show()

The child replaces the parent's implementation.

14. Difference Between Overriding and Overloading
Overriding	Overloading
Parent and child classes	Same class
Same method	Same method name
Child replaces parent	Different parameters
Supported in Python	Traditional overloading is not directly supported in Python; similar behavior is achieved using default arguments, *args, or **kwargs
15. Good Coding Practices Learned Today

✅ Validate input before processing.

✅ Keep important data private.

✅ Avoid duplicate variables.

❌ Avoid

self.balance = self.__balance

when self.__balance already exists.

Use meaningful messages.

Instead of

Invalid Input

Use

Insufficient Balance

Invalid Amount
16. Python Style (PEP 8)

Instead of

if(amount>0):

Write

if amount > 0:

Instead of

if(amount>0 and amount<=balance):

Write

if amount > 0 and amount <= balance:

Readable code is professional code.

17. Key Takeaways
Encapsulation protects data from direct modification.
Private variables use double underscores (__).
Access data through methods rather than directly.
Always validate user input.
Think about edge cases before finalizing logic.
super() calls the specified parent method.
Writing correct logic is more important than memorizing syntax.

📘 Python Development Journey – Day 6 Notes
Topic: OOP Practice – Bank Management System
1. What did we learn today?

Today was not about learning a new Python concept.

Today was about applying everything learned in the previous five days to build a real-world application.

We designed and implemented a Bank Management System using Object-Oriented Programming.

2. OOP Design Process

Before writing code, always ask these questions:

Step 1

What is my object?

Example:

BankAccount
Step 2

What data should this object store?

Example:

Name
Account Number
Bank Name
Balance

These become attributes.

Step 3

What actions can this object perform?

Example:

Deposit Money

Withdraw Money

Display Details

These become methods.

3. Constructor Design

A constructor initializes the object when it is created.

Example

def __init__(self, name, account_number, bank_name, balance):

The constructor should receive all information necessary to create a complete object.

4. Public vs Private Variables
Public Variables

Accessible from anywhere.

Example

self.name
self.bank_name

Used for information that does not require strict protection.

Private Variables

Protected from direct modification.

Example

self.__balance

self.__account_number

Used for sensitive information.

5. Why is Balance Private?

Balance should never be changed directly.

Incorrect

account.__balance = 100000

Correct

deposit()

withdraw()

This protects the integrity of the object.

6. Constructor Execution

When we write

s1 = BankAccount(...)

Python internally performs

BankAccount.__init__(s1, ...)

This is why self refers to the current object.

7. Understanding self

self is not a keyword.

It is simply the first parameter that receives the object calling the method.

Example

s1.display()

Internally becomes

BankAccount.display(s1)

Therefore

self

becomes

s1
8. Designing Methods

Every method should answer three questions:

What input does it need?

Example

deposit(amount)
What should it validate?

Example

amount > 0
What object data should it modify?

Example

self.__balance
9. Input Validation

Never trust user input.

Example

deposit(-500)

Should be rejected.

Example

withdraw(-200)

Should be rejected.

Example

withdraw(100000)

Should also be rejected if balance is insufficient.

10. Good Error Messages

Avoid

Invalid Input

Prefer

Deposit amount must be positive

Withdrawal amount must be positive

Insufficient Balance

Specific messages improve user experience.

11. Encapsulation

Encapsulation means

Keeping data and methods together inside a class.
Protecting important data from direct access.
Allowing modifications only through controlled methods.

Example

Deposit

Withdraw

instead of directly modifying

Balance
12. Professional Coding Practices Learned Today
Meaningful Method Names

Good

deposit()

withdraw()

display()

Bad

fun1()

abc()
Validate Before Updating

Always

Validate

↓

Modify Object

↓

Display Success

Never update object data before validation.

Protect Sensitive Information

Private variables should be used when the data must remain secure.

13. Interview Questions
Q1

What is Object-Oriented Programming?

Q2

Why do we use constructors?

Q3

Why is self required?

Q4

Difference between public and private variables.

Q5

Explain encapsulation using BankAccount.

Q6

Why should balance be private?

Q7

What happens internally when

account.deposit(500)

is executed?

Q8

Can private variables be accessed inside the class?

Q9

Why do we validate input?

Q10

What are the responsibilities of a constructor?

14. Common Mistakes

❌ Hardcoding values

self.__balance = 1000

Instead of

self.__balance = balance

❌ Forgetting validation

withdraw(-500)

❌ Accessing object data without self

Incorrect

balance += amount

Correct

self.__balance += amount

❌ Making every variable public

Sensitive data should remain private.

15. Mentor's Key Takeaway

Today, you learned one of the most important lessons in software engineering:

Think before you code.

The process is:

Problem

↓

Identify Objects

↓

Identify Data

↓

Identify Behaviours

↓

Design Constructor

↓

Write Methods

↓

Validate Input

↓

Review & Improve

This design-first mindset is what separates developers from people who only memorize syntax.

Topic: Composition (HAS-A Relationship)

Project: Library Management System

1. What is Composition?

Composition is an OOP concept in which one class contains objects of another class.

It represents a HAS-A relationship.

Definition

Composition means creating a class that uses one or more objects of another class as its members.

2. HAS-A Relationship

Examples:

Car HAS-A Engine

Library HAS-A Books

University HAS-A Students

Hospital HAS-A Patients

Playlist HAS-A Songs

Notice that none of these objects inherit from each other.

They simply contain other objects.

3. Composition vs Inheritance
Composition

Relationship:

HAS-A

Example

Library HAS-A Book

Purpose

Objects work together.
One object contains another object.
Inheritance

Relationship

IS-A

Example

Dog IS-A Animal

Purpose

Code reuse.
Parent-child relationship.
4. Why Use Composition?

Composition helps us:

Organize software into multiple classes.
Keep responsibilities separate.
Reuse objects.
Build scalable applications.
Follow good software design.
5. Store Objects Instead of Data

Instead of

books = [
    "Python",
    "Java"
]

Prefer

books = [
    Book(...),
    Book(...)
]
Why?

A Book object contains:

Book Name
Author
Book ID
Availability
Methods

Storing only the name loses all other information.

6. Library Design

The Library class should not store:

Book Name
Author
Book ID

Instead it should store

self.books = []

which is a list of Book objects.

7. Responsibilities of Classes
Book

Responsible for:

Storing book details.
Displaying book information.
Managing book-related behavior.
Library

Responsible for:

Managing a collection of books.
Adding books.
Displaying all books.
Searching books.

The library should not manage the internal details of a book.

8. Encapsulation + Composition

Private data should remain inside the class.

Incorrect

book.__Book_ID

Correct

book.display_book_info()

The object itself should manage its private data.

9. Why Use a List?

Instead of

self.book1
self.book2
self.book3

Use

self.books = []

Advantages:

Unlimited number of books.
Easy to add/remove books.
Cleaner code.
Scalable.
10. Why Not Store Number of Books?

Avoid

self.number_of_books

because

len(self.books)

already gives the count.

Principle

Do not store duplicate information if it can be calculated.

11. Constructor Design

Book

Book(name, author, id)

Availability should automatically start as

True

A new book should be available by default.

Library

Library(name)

Initialize

self.books = []

The library starts empty and books are added later.

12. Composition Diagram
Library
│
├── library_name
│
└── books
      │
      ├── Book Object
      ├── Book Object
      ├── Book Object
      └── Book Object

This is the visual representation of Composition.

13. Interview Questions
Q1. What is Composition?

Answer:
Composition is an OOP concept where one class contains objects of another class, representing a HAS-A relationship.

Q2. Difference between Composition and Inheritance?

Composition

HAS-A relationship
One object contains another object
More flexible

Inheritance

IS-A relationship
Child inherits from parent
Used for code reuse
Q3. Why does Library store Book objects instead of book names?

Answer:
A Book object stores all related information (title, author, ID, availability) and methods. Storing only names would lose this information.

Q4. Why is self.books a list?

Answer:
A library can have any number of books. A list allows dynamic addition and removal of Book objects.

Q5. Why shouldn't Library directly access private variables of Book?

Answer:
Private variables are protected by encapsulation. The Book class should provide methods to interact with its own data.

Q6. Why is display_book_info() inside the Book class?

Answer:
A Book object knows its own details. This follows the Single Responsibility Principle, where each class manages its own responsibilities.

14. Key Takeaways
Composition represents a HAS-A relationship.
Store objects, not just primitive data.
A class should have one clear responsibility.
Use lists to manage multiple objects.
Protect private data using encapsulation.
Design objects that collaborate rather than one class doing everything.