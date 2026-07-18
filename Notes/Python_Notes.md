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

📒 Day 8 Notes (Interview Revision)
1. Why File Handling?
Variables are stored in RAM.
RAM is temporary.
Files provide permanent storage.
2. File Modes
Mode	Purpose	If file doesn't exist	If file exists
r	Read	❌ Error	Opens for reading
w	Write	✅ Creates file	Overwrites existing content
a	Append	✅ Creates file	Adds data at the end
3. open()
file = open("notes.txt", "r")
Opens the file.
Returns a file object.
Does not read the contents.
4. read()
content = file.read()
Reads the entire file.
Returns a string.
5. write()
file.write("Hello")
Writes data to the file.
6. close()
file.close()
Releases system resources.
Ensures data is saved properly.
7. with open()
with open("notes.txt", "r") as file:
    content = file.read()
Automatically closes the file.
Preferred in professional Python code.
8. File Pointer
read() moves the file pointer to the end.
Calling read() again returns an empty string.
Reading after close() raises an error.

📒 Day 9 Notes – Exception Handling (Python)
Prepared by your Python Mentor 🤝
🎯 What is an Exception?

An Exception is a runtime error that occurs while a program is executing and interrupts the normal flow of the program.

Examples
10 / 0

➡️ ZeroDivisionError

int("Surya")

➡️ ValueError

file = open("abc.txt", "r")

(If the file doesn't exist)

➡️ FileNotFoundError

🎯 Why Do We Use Exception Handling?

Without exception handling:

❌ Program crashes.
❌ Poor user experience.
❌ Remaining code doesn't execute.

With exception handling:

✅ Program continues running.
✅ Displays meaningful error messages.
✅ Makes applications more robust and professional.
🏦 Real-Life Analogy

Think of an ATM.

Normal Flow
Insert Card
      ↓
Enter PIN
      ↓
Withdraw Money

If you enter the wrong PIN:

❌ ATM doesn't crash.

✅ It displays:

Incorrect PIN. Please try again.

This is exactly what exception handling does.

🎯 try

The try block contains the code that might cause an exception.

try:
    age = int(input("Enter age: "))

Meaning:

"Try to execute this code."

🎯 except

The except block executes only if an exception occurs.

try:
    age = int(input())

except:
    print("Invalid input")

Meaning:

"If an error occurs, handle it here."

🎯 Catching Specific Exceptions

Instead of handling all errors together:

except:

Professional code catches specific exceptions.

Example:

except ValueError:
except ZeroDivisionError:

Advantages:

More readable.
Better debugging.
Better user experience.
Industry best practice.
🎯 Common Exceptions
1. ValueError

Occurs when the value is invalid.

Example:

int("Surya")

Reason:

The type is acceptable (str), but the value cannot be converted into an integer.

2. ZeroDivisionError

Occurs when dividing by zero.

Example:

100 / 0
3. TypeError

Occurs when incompatible types are used.

Example:

"Hello" + 5

Reason:

String and integer cannot be added together.

🧠 Difference Between ValueError and TypeError
ValueError	TypeError
Correct type, wrong value	Wrong data type
int("Surya")	"Hello" + 5

Easy Trick:

ValueError → Right type, wrong value.
TypeError → Wrong type.
🎯 else

The else block executes only if no exception occurs.

Example:

try:
    x = int(input())

except ValueError:
    print("Invalid")

else:
    print("Input accepted")

If the input is:

25

Output:

Input accepted
🎯 finally

The finally block executes always, regardless of whether an exception occurs.

Example:

try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program ended")

Output:

Cannot divide by zero
Program ended
🎯 Flow of Exception Handling
          try
           │
           ▼
   Is there an exception?
      /            \
    No              Yes
    │               │
    ▼               ▼
  else           except
      \          /
       \        /
        ▼      ▼
        finally
🎯 Complete Example
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = x / y
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input! Please enter numbers only.")

else:
    print("Division successful.")

finally:
    print("Program ended.")
🎯 Interview Questions
Q1. What is an Exception?

An exception is a runtime error that interrupts the normal execution of a program.

Q2. Why do we use try-except?

To handle runtime errors gracefully, prevent program crashes, and provide meaningful feedback to the user.

Q3. Difference between try and except?
try → Contains code that might raise an exception.
except → Handles the exception if it occurs.
Q4. When does else execute?

Only when no exception occurs in the try block.

Q5. When does finally execute?

Always, whether an exception occurs or not.

💡 Key Takeaways
✔ Exceptions are runtime errors.
✔ try contains risky code.
✔ except handles errors.
✔ Catch specific exceptions whenever possible.
✔ else runs only if the try block succeeds.
✔ finally runs in every situation.
✔ Exception handling makes programs robust, user-friendly, and professional.

📒 Day 10 Notes – Python (raise) + AI Foundation (Machine Learning vs Deep Learning)

Prepared by your Mentor 🤝

🐍 Python: raise Keyword
🎯 What is raise?

The raise keyword is used to manually generate an exception when our program detects an invalid condition.

Syntax:

raise ExceptionType("Error Message")

Example:

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")
🤔 Why do we use raise?

Python automatically raises exceptions like:

int("Surya")          # ValueError
10 / 0                # ZeroDivisionError

But Python doesn't know our business rules.

Example:

deposit = -500

Python thinks this is just a number.

We know this is invalid.

So we manually raise an exception.

🏦 Real-Life Analogy

Imagine you're a bank manager.

Customer:

Deposit = -500

You immediately stop the transaction.

This is exactly what raise does.

🎯 Using raise with try-except
try:
    amount = int(input("Enter amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive.")

except ValueError as e:
    print(e)
🎯 Exception Object (as e)
except ValueError as e:
    print(e)

e stores the error message.

Example:

raise ValueError("Invalid marks")

Output:

Invalid marks
🧠 Difference Between print() and raise

❌ Only displays a message:

print("Age cannot be negative")

✅ Creates an actual exception:

raise ValueError("Age cannot be negative.")

Remember:

print() informs the user.

raise informs Python.

🎯 Complete Flow
try
   │
   ▼
Input
   │
   ▼
Business Rule Check
   │
   ├── Valid → else
   │
   └── Invalid → raise
                    │
                    ▼
               except
                    │
                    ▼
                finally
🤖 AI Foundation
What is Machine Learning?

Machine Learning is a subset of AI where computers learn patterns from data instead of following manually written rules.

Example:

Thousands of Cat Images
        ↓
Machine Learning
        ↓
Model
        ↓
New Image
        ↓
Prediction
What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses deep neural networks to automatically learn complex patterns from large amounts of data.

🌳 AI Hierarchy
Artificial Intelligence
│
├── Rule-Based AI
│
└── Machine Learning
      │
      ├── Linear Regression
      ├── Decision Trees
      ├── Random Forest
      │
      └── Deep Learning
             │
             ├── CNN
             ├── RNN
             ├── LSTM
             └── Transformers (ChatGPT)
🆚 Machine Learning vs Deep Learning
Machine Learning	Deep Learning
Subset of AI	Subset of Machine Learning
Works well with smaller datasets	Needs large datasets
Often requires manual feature engineering	Learns features automatically
Faster to train	More computationally expensive
Simpler models	Deep Neural Networks
🎯 Traditional Programming vs Machine Learning
Traditional Programming
Data + Rules
      ↓
   Output

The programmer writes the rules.

Machine Learning
Data + Correct Answers
         ↓
      Learning
         ↓
       Model
         ↓
     Prediction

The computer learns the rules.

🎯 Why Deep Learning?

Instead of manually writing rules like:

Two ears
Four legs
Tail

Deep Learning learns these features automatically from millions of images.

This makes it much better at handling:

Different angles
Different lighting
Occlusions
Background changes
New unseen images
🧠 The Most Important Word
Generalization

Definition:

The ability of a model to correctly predict outcomes for new, unseen data after learning from training data.

Example:

The model has never seen this exact cat image before.

It still predicts:

"This is a cat."

That is generalization.

🏆 Golden Rules (Write These in Your Notebook)
Rule 1

Artificial Intelligence aims to make machines perform tasks requiring human intelligence.

Rule 2

Machine Learning learns patterns from data.

Rule 3

Deep Learning automatically learns complex patterns using deep neural networks.

Rule 4

Deep Learning performs best when large amounts of data are available.

Rule 5

Generalization is the ability to perform well on unseen data.

🎯 Interview Questions
Q1. What is the raise keyword?

The raise keyword is used to manually generate an exception when a program detects an invalid condition.

Q2. Difference between print() and raise?
print() displays a message.
raise creates an actual exception.
Q3. What is Machine Learning?

A subset of AI where computers learn patterns from data instead of following manually written rules.

Q4. What is Deep Learning?

A subset of Machine Learning that uses deep neural networks to automatically learn complex patterns from large datasets.

Q5. What is Generalization?

The ability of a trained model to make accurate predictions on unseen data.

📒 Day 11 Notes – Modules, Imports & AI Foundations

Prepared by your Mentor 🤝

🐍 Python – Modules
📦 What is a Module?

A module is simply a Python file (.py) that contains reusable code such as:

Functions
Classes
Variables

Example:

calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

Here, calculator.py is a module.

🎯 Why Do We Use Modules?

Without modules:

❌ Copy-paste code into every project.

With modules:

✅ Write once.

✅ Reuse everywhere.

Benefits:

Reusability
Better organization
Easy maintenance
Less code duplication
Industry standard
📥 Importing Modules
Method 1: Import the Whole Module
import calculator

print(calculator.add(5, 3))

Use:

module_name.function_name()
Method 2: Import Specific Functions
from calculator import add, subtract

print(add(5, 3))

No need to write:

calculator.add()
Method 3: Import with Alias
import numpy as np
np.array([1, 2, 3])

Alias = Short name for a module.

Examples:

import pandas as pd
import matplotlib.pyplot as plt

These are industry conventions.

🔹 Dot Notation (.)

When you import a module:

import calculator

Access its functions using:

calculator.add()
calculator.subtract()

The . operator accesses members inside the module.

🎯 Built-in Modules

Python already provides many modules.

Example:

import math

print(math.sqrt(25))

Output:

5.0

Common built-in modules:

math
random
os
datetime
🤖 AI Foundation
AI vs Machine Learning vs Data Science
📊 Data Science

Focus:

Collecting data
Cleaning data
Data visualization
Finding insights

Example:

Which product sells the most?
Customer behavior analysis
🤖 Machine Learning

Focus:

Learning patterns from data
Building predictive models

Example:

Predict:

Spam email
House price
Customer purchase
🧠 AI

Focus:

Building intelligent systems that can:

Understand language
Recognize images
Make decisions
Solve problems

Examples:

ChatGPT
Self-driving cars
Face recognition
Robotics
🌳 Relationship
Artificial Intelligence
│
├── Machine Learning
│      │
│      └── Deep Learning
│
└── Other AI Techniques

Data Science overlaps with AI and ML by providing high-quality data and insights.

🧠 Mathematics in AI

Mathematics is the foundation of AI.

Without mathematics:

❌ Can use libraries.

✅ Cannot understand algorithms.

1️⃣ Linear Algebra

Used for:

Vectors
Matrices
Images
Neural Networks

Example:

An image is represented as a matrix of pixel values.

2️⃣ Probability

Used to measure confidence.

Example:

Cat → 95%
Dog → 5%

The model predicts probabilities instead of just labels.

3️⃣ Calculus

Used to:

Reduce error
Update model parameters
Train neural networks

Important concept:

Gradient Descent

We'll study this later.

🎯 Why AI Gives Probabilities

Instead of:

Cat

AI predicts:

Cat → 90%
Dog → 10%

Reason:

The model expresses its confidence in each prediction.

This helps humans make informed decisions, especially in uncertain situations (e.g., medical diagnosis).

🌟 Important Keywords
Module

A Python file containing reusable code.

Import

Brings code from another module into the current program.

Alias

A shorter name for a module.

Example:

import numpy as np
Data Scientist

Works with data:

Collection
Cleaning
Visualization
Insights
Machine Learning Engineer

Builds models that:

Learn patterns
Make predictions
Generalize to unseen data
AI Engineer

Builds intelligent applications using AI/ML models.

Examples:

Chatbots
Robotics
Computer Vision
NLP
Probability

Represents the confidence of a prediction.

Generalization

The ability of a trained model to perform well on new unseen data.

🏆 Interview Questions
Q1. What is a module?

A Python file containing reusable functions, classes, or variables.

Q2. Difference between:
import math

and

from math import sqrt
import math imports the whole module.
from math import sqrt imports only the sqrt function.
Q3. Why do we use aliases?

To make code shorter and more readable.

Example:

import numpy as np
Q4. Difference between Data Science, ML, and AI?
Data Science → Works with data.
Machine Learning → Learns patterns and builds predictive models.
AI → Builds intelligent systems.
Q5. Why is Mathematics important in AI?

Because AI algorithms rely on:

Linear Algebra
Probability
Calculus

to learn, optimize, and make predictions.

📒 Day 12 Notes – Packages & Machine Learning Fundamentals

Prepared for: Surya Rathore 🤝

🐍 Python Development
📦 Packages
What is a Package?

A Package is a folder that contains multiple related Python modules.

Example:

Math/
│── calculator.py
│── geometry.py
│── statistics.py
│── __init__.py

Here:

calculator.py → Module
geometry.py → Module
statistics.py → Module

The Math folder is the Package.

📝 Module vs Package
Module	Package
A single .py file	A folder containing related modules
Contains functions/classes	Contains multiple modules
Example: calculator.py	Example: Math/
🎯 Why Do We Use Packages?

Without packages:

calculator.py
geometry.py
matrix.py
vectors.py
probability.py
linear_algebra.py
...

Everything is in one folder.

Problems:

Difficult to manage
Hard to find files
Poor organization

With packages:

Project/
│
├── Math/
│     calculator.py
│     geometry.py
│
├── AI/
│     matrix.py
│     vectors.py
│
├── Data/
│     preprocessing.py
│
└── main.py

Benefits:

✅ Organized code
✅ Easy maintenance
✅ Easy navigation
✅ Industry standard
✅ Scalable for large projects
📚 Built-in Modules

Python already provides many useful modules.

1. math

Used for mathematical operations.

Example:

import math

print(math.sqrt(25))
print(math.pow(2, 5))
print(math.pi)
2. random

Used to generate random values.

Example:

import random

print(random.randint(1, 100))
3. datetime

Used for date and time.

Example:

from datetime import datetime

print(datetime.now())
4. os

Used for operating system-related tasks.

Example:

import os

print(os.getcwd())
💻 Coding Practice

Created:

math_utils.py
import math

def square_root(num):
    return math.sqrt(num)

def power(a, b):
    return math.pow(a, b)
main.py
from math_utils import square_root, power

num = float(input("Enter a number: "))
print("Square Root:", square_root(num))

a = float(input("Enter base: "))
b = float(input("Enter exponent: "))

print("Power:", power(a, b))
🤖 Machine Learning Fundamentals
📊 What is a Dataset?

A Dataset is a collection of data organized into rows and columns.

Example:

Color	Weight	Shape	Fruit
Red	180	Round	Apple
Yellow	120	Long	Banana
Orange	170	Round	Orange

The entire table is called a Dataset.

🎯 Features

A Feature is an input variable used by the model to make predictions.

Examples:

Age
Height
Salary
Weight
Color
Shape

Think:

Feature = Input

🏷️ Label (Target)

A Label is the correct output that the model tries to predict.

Examples:

Apple
Banana
Pass
Fail
House Price
Spam

Think:

Label = Output

🍎 Example
Color	Weight	Shape	Fruit
Red	180	Round	Apple
Features
Color
Weight
Shape
Label
Apple
👨‍🎓 Student Example
Study Hours	Attendance	Assignments	Result
8	95%	Yes	Pass

Features:

Study Hours
Attendance
Assignments

Label:

Pass
🚗 Self-Driving Car Example

Features:

Traffic Light = Red
Speed = 45 km/h
Pedestrian = Yes

Label:

Brake
🧠 How Does Machine Learning Learn?

Machine Learning does not memorize the dataset.

Instead, it learns patterns.

Example:

Hours Studied	Result
8	Pass
7	Pass
6	Pass
2	Fail
1	Fail

The model learns a pattern like:

Students who study more are more likely to pass.

🌟 Pattern Learning

Machine Learning finds relationships between:

Features

↓

Labels

instead of remembering every row.

🎯 Generalization

Definition:

The ability of a Machine Learning model to perform well on new unseen data.

Example:

Training Data:

6 hrs → Pass
7 hrs → Pass
2 hrs → Fail

New Student:

5 hrs → ?

The model predicts using learned patterns.

This is called Generalization.

❌ Memorization vs ✅ Generalization
Memorization
Learns exact rows.
Fails on new data.
Causes Overfitting.
Generalization
Learns patterns.
Works on unseen data.
Goal of Machine Learning.
🧩 Machine Learning Pipeline
Dataset
   │
   ▼
Features (Input)
   │
   ▼
Machine Learning Model
   │
   ▼
Learns Patterns
   │
   ▼
Predicts Label
🌟 Important Keywords
Dataset

A collection of data arranged in rows and columns.

Feature

Input variables used for prediction.

Label

Correct output that the model predicts.

Pattern Learning

Finding relationships between features and labels.

Generalization

Making good predictions on new unseen data.

Package

A folder containing related Python modules.

Module

A single Python (.py) file containing reusable code.

🏆 Interview Questions
Q1. What is the difference between a Module and a Package?

Answer:

Module → A single Python (.py) file.
Package → A folder containing related modules.
Q2. What is a Dataset?

A collection of data organized into rows and columns.

Q3. What is a Feature?

An input variable used by the model to make predictions.

Q4. What is a Label?

The correct output that the model learns to predict.

Q5. Does Machine Learning memorize data?

No.

It learns patterns from the data and uses those patterns to make predictions on new unseen data.

Q6. What is Generalization?

The ability of a trained model to perform well on unseen data.


📒 Day 13 Notes – Lambda Functions & Machine Learning (Training vs Testing)

90-Day Python + AI/ML Roadmap
Student: Surya Rathore
Day: 13 ✅

🐍 Python Development
🔹 Lambda Functions
What is a Lambda Function?

A Lambda Function is a small anonymous function that can be written in one line.

It is mainly used for short and temporary operations.

Syntax
lambda parameters: expression

Example:

square = lambda x: x*x
print(square(5))

Output:

25
🔹 Normal Function vs Lambda Function
Normal Function
def square(x):
    return x*x

print(square(5))
Lambda Function
square = lambda x: x*x

print(square(5))
Difference
Normal Function	Lambda Function
Uses def	Uses lambda
Multiple lines	Single line
Uses return	No explicit return
Best for reusable functions	Best for short, temporary functions
🔹 Examples
Square
square = lambda x: x*x
print(square(4))

Output

16
Cube
cube = lambda x: x**3
print(cube(3))

Output

27
Addition
add = lambda a,b: a+b
print(add(10,20))

Output

30
Maximum of Two Numbers
maximum = lambda a,b: a if a>b else b

print(maximum(10,20))

Output

20
Positive Number Check
positive = lambda x:x>0

print(positive(5))
print(positive(-3))

Output

True
False
💡 Advantages of Lambda Functions
Short and readable
Less code
Useful for temporary functions
Commonly used with functions like map(), filter(), and sorted() (we'll learn these later)
🤖 Machine Learning
📊 Training Data

Training Data is the part of the dataset used to teach the Machine Learning model.

The model learns:

Patterns
Relationships
Rules

Example:

Hours Studied	Result
8	Pass
7	Pass
2	Fail

The model studies these examples to learn the relationship between study hours and result.

📝 Testing Data

Testing Data is not shown to the model during training.

It is used only after training to check whether the model has learned correctly.

Purpose:

Evaluate the model
Measure prediction accuracy
Check generalization
📈 Dataset Split

Example:

Dataset = 1000 rows

1000 Rows
│
├── 800 → Training Data
│
└── 200 → Testing Data

Typical split:

80% Training
20% Testing

(Other ratios like 70:30 or 90:10 are also used depending on the problem.)

🎯 Why Do We Split the Dataset?

If we train and test on the same data:

The model may simply memorize the answers.
It may appear to perform perfectly.
We cannot know whether it can handle new unseen data.

Therefore, we always evaluate using Testing Data.

🧠 Generalization

Generalization means:

The ability of a model to perform well on new unseen data.

Goal of every Machine Learning model:

✔ Learn patterns, not memorize examples.

❌ Overfitting

Definition:

A model that performs very well on training data but poorly on testing data.

Reason:

It memorizes the training data instead of learning general patterns.

Example:

Training Accuracy = 99%

Testing Accuracy = 52%

This indicates Overfitting.

🧩 Codeforces Analogy
Training Data

The Codeforces problems you've already solved.

Examples:

Binary Search
Greedy
Prefix Sum
Monotonic Stack
Testing Data

The new contest problems that you've never seen before.

If you solve them successfully:

✔ You generalized.

If you can only solve previously seen problems:

❌ You are overfitting.

🧠 Machine Learning Pipeline (So Far)
Dataset
   │
   ▼
Split Dataset
   │
   ├──────────────┐
   │              │
   ▼              ▼
Training Set   Testing Set
   │              │
   ▼              │
Learn Patterns    │
   │              │
   └──────► Evaluate Model
                    │
                    ▼
          Predict New Data
🌟 Key Terms
Dataset

Collection of data arranged in rows and columns.

Feature

Input variables used by the model.

Examples:

Age
Salary
Weight
Label

Correct output the model learns to predict.

Examples:

Pass/Fail
Apple/Banana
House Price
Training Data

Data used to teach the model.

Testing Data

Data used to evaluate the model.

Generalization

Ability to perform well on unseen data.

Overfitting

Memorizing the training data instead of learning patterns.

💼 Interview Questions
Q1. What is a Lambda Function?

A lambda function is a small anonymous function written in a single line using the lambda keyword.

Q2. Difference between a normal function and a lambda function?
Normal Function	Lambda Function
Uses def	Uses lambda
Multi-line	Single-line
Explicit return	Implicit return
Best for reusable code	Best for short tasks
Q3. What is Training Data?

Training Data is the data used to teach a Machine Learning model by helping it learn patterns.

Q4. What is Testing Data?

Testing Data is unseen data used to evaluate the model after training.

Q5. Why do we split a dataset?

To check whether the model has learned patterns instead of memorizing the training data.

Q6. What is Generalization?

The ability of a Machine Learning model to perform well on new unseen data.

Q7. What is Overfitting?

Overfitting occurs when a model performs very well on training data but poorly on testing data because it memorizes the training data instead of learning patterns.


📒 Day 14 Notes – map() Function & Machine Learning Workflow

90-Day Python + AI/ML Roadmap
Student: Surya Rathore
Day: 14 ✅

🐍 Python Development
🔹 map() Function
What is map()?

map() is a built-in Python function that applies the same function to every element of an iterable (list, tuple, etc.).

It helps write shorter, cleaner, and more readable code.

Syntax
map(function, iterable)
function → The operation to perform.
iterable → The collection (list, tuple, etc.) to process.

Since map() returns a map object, we usually convert it to a list:

list(map(function, iterable))
🔹 Example 1 – Double Every Number
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)

Output:

[2, 4, 6, 8]
🔹 Example 2 – Square Every Number
numbers = [2, 4, 6, 8]

result = list(map(lambda x: x**2, numbers))

print(result)

Output:

[4, 16, 36, 64]
🔹 Example 3 – Convert Strings to Uppercase
names = ["surya", "iiitdm", "python"]

result = list(map(lambda x: x.upper(), names))

print(result)

Output:

['SURYA', 'IIITDM', 'PYTHON']
🔹 Example 4 – GST Calculation
prices = [100, 250, 400, 150]

new_prices = list(map(lambda x: x * 1.18, prices))

print(new_prices)

Output:

[118.0, 295.0, 472.0, 177.0]
🔹 for Loop vs map()
for Loop	map()
More code	Less code
Manual iteration	Automatic iteration
Flexible	Best for applying one function to all elements
Beginner-friendly	Cleaner for simple transformations
💡 Advantages of map()
Shorter code
Better readability
Efficient for applying the same operation
Often used with lambda functions
Common in data processing pipelines
🤖 Machine Learning
🔹 Complete Machine Learning Workflow

Every ML project follows a sequence of steps.

Collect Data
      ↓
Clean Data
      ↓
Split Data
      ↓
Train Model
      ↓
Test Model
      ↓
Predict New Data
1️⃣ Collect Data

The first step is to collect relevant data.

Example:

Study Hours	Attendance	Result
8	95%	Pass
2	50%	Fail

Without data, the model cannot learn.

2️⃣ Clean Data

Real-world data often contains:

Missing values (NULL, ?)
Invalid values (e.g., Age = -10)
Duplicate records
Incorrect formats

Before training, we clean the data.

Example:

Age	Salary
24	₹5 LPA
-10	₹7 LPA

Age cannot be negative, so this record must be corrected or removed.

💡 Garbage In, Garbage Out (GIGO)

If poor-quality data is used for training:

➡️ Poor-quality predictions will be produced.

Good data leads to better models.

3️⃣ Split Data

After cleaning, the dataset is divided into:

Training Data (usually 80%)
Testing Data (usually 20%)

Example:

1000 Rows
│
├── 800 → Training
│
└── 200 → Testing

Purpose:

Train on one part
Evaluate on another
4️⃣ Train Model

The model studies the training data and learns patterns.

Example:

Hours Studied	Result
8	Pass
2	Fail

The model learns:

Students who study more are more likely to pass.

5️⃣ Test Model

The model is tested using unseen data.

Example:

Hours Studied	Result
5	?

The model predicts:

Pass

We compare the prediction with the actual answer to evaluate performance.

6️⃣ Predict New Data

After successful testing, the model is used in the real world.

Example:

A new student:

Hours Studied	Attendance
7	92%

Prediction:

Pass

This stage is also called Inference.

🌟 ML Workflow Summary
Collect Data
      ↓
Clean Data
      ↓
Split Data
      ↓
Train Model
      ↓
Test Model
      ↓
Deploy / Predict New Data
🔑 Important Terms
Dataset

A collection of organized data.

Data Cleaning

Removing or correcting invalid, missing, or duplicate data.

Training Data

Data used to teach the model.

Testing Data

Data used to evaluate the model.

Generalization

Ability to perform well on unseen data.

Overfitting

When the model memorizes training data instead of learning patterns.

Inference

Using the trained model to make predictions on new data.

💼 Interview Questions
Q1. What does map() do?

It applies a function to every element of an iterable and returns a map object.

Q2. Why do we use list() with map()?

Because map() returns a map object, not a list. list() converts it into a list.

Q3. What is the first step in a Machine Learning project?

Collecting data.

Without data, the model cannot learn.

Q4. Why is data cleaning important?

To remove incorrect, missing, or invalid data so the model learns from high-quality information.

Q5. Why do we split the dataset?

To train the model on one portion and evaluate it on unseen data.

Q6. What is inference?

Inference is the process of using a trained model to make predictions on new unseen data.

📒 Day 15 Notes – filter() Function & Types of Machine Learning

90-Day Python + AI/ML Roadmap
Student: Surya Rathore
Day: 15 ✅

🐍 Python Development
🔹 filter() Function
What is filter()?

filter() is a built-in Python function that selects only those elements that satisfy a given condition.

Unlike map(), which transforms every element, filter() removes elements that do not satisfy the condition.

Syntax
filter(function, iterable)

Since filter() returns a filter object, we usually convert it into a list.

list(filter(function, iterable))
🔹 Example 1 – Keep Even Numbers
numbers = [5, 8, 12, 15, 20, 23]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

Output

[8, 12, 20]
🔹 Example 2 – Keep Positive Numbers
numbers = [-10, 5, -3, 8, 0, 12]

result = list(filter(lambda x: x > 0, numbers))

print(result)

Output

[5, 8, 12]

Note: 0 is neither positive nor negative.

🔹 Example 3 – Keep Long Strings
students = ["Ram", "Shyam", "Python", "AI", "ML", "Machine Learning"]

result = list(filter(lambda x: len(x) > 4, students))

print(result)

Output

['Shyam', 'Python', 'Machine Learning']
🔹 map() vs filter()
map()	filter()
Transforms every element	Selects matching elements
Output size usually remains the same	Output size may decrease
Returns modified elements	Returns only elements satisfying a condition

Example:

numbers = [1, 2, 3, 4]
map()
list(map(lambda x: x * 2, numbers))

Output

[2, 4, 6, 8]
filter()
list(filter(lambda x: x % 2 == 0, numbers))

Output

[2, 4]
💡 Advantages of filter()
Cleaner code
Easy selection of required elements
Frequently used in data preprocessing
Works well with lambda functions
🤖 Machine Learning
🔹 Types of Machine Learning

Machine Learning is broadly divided into three major categories.

Machine Learning
│
├── Supervised Learning
├── Unsupervised Learning
└── Reinforcement Learning
1️⃣ Supervised Learning
Definition

Supervised Learning is a type of Machine Learning where the model learns from labeled data.

The dataset contains:

Input (Features)
Correct Output (Labels)

The model learns the relationship between inputs and outputs.

Example
Study Hours	Result
8	Pass
2	Fail
6	Pass

Feature:

Study Hours

Label:

Result

The model learns to predict the result for new students.

Real-Life Examples
Spam Email Detection
House Price Prediction
Disease Prediction
Cat vs Dog Image Classification
2️⃣ Unsupervised Learning
Definition

Unsupervised Learning is a type of Machine Learning where the dataset contains only input features.

There are no labels.

The model discovers hidden patterns or groups similar data.

Example
Age	Salary
22	₹4 LPA
24	₹5 LPA
50	₹20 LPA

No labels such as:

Premium Customer
Regular Customer

The model groups similar customers automatically.

Real-Life Examples
Customer Segmentation
Market Basket Analysis
Document Clustering
Fraud Pattern Discovery
3️⃣ Reinforcement Learning
Definition

Reinforcement Learning is a type of Machine Learning where an agent learns through trial and error.

The agent interacts with the environment and receives:

Reward for correct actions
Penalty for incorrect actions

The objective is to maximize total reward.

Example

Robot Learning

Walk correctly → Reward
Fall down → Penalty

The robot gradually improves its behavior.

Real-Life Examples
Self-Driving Cars
Chess AI
Robot Navigation
Game Playing AI
Robotic Dogs
📊 Comparison
Supervised	Unsupervised	Reinforcement
Has labels	No labels	Reward & Penalty
Learns from examples	Finds hidden patterns	Learns through trial and error
Predicts outputs	Groups similar data	Learns best actions
🔑 Important Terms
Feature

Input variables used by the model.

Examples:

Age
Salary
Study Hours
Label

Correct output associated with each example.

Examples:

Pass/Fail
Spam/Not Spam
Cat/Dog
Agent

The learner in Reinforcement Learning.

Examples:

Robot
Self-driving car
Chess-playing AI
Environment

The world in which the agent performs actions.

Reward

Positive feedback for a correct action.

Penalty

Negative feedback for an incorrect action.

🧠 Real-Life Analogy
Supervised Learning

Teacher gives:

Question
Correct Answer

Student learns from examples.

Unsupervised Learning

Teacher gives only questions.

Student groups similar questions by finding patterns.

Reinforcement Learning

Teacher gives:

Reward for correct answer
Penalty for wrong answer

Student improves through trial and error.

💼 Interview Questions
Q1. What is filter()?

filter() selects only those elements that satisfy a specified condition.

Q2. Difference between map() and filter()?
map()	filter()
Modifies all elements	Selects matching elements
Transformation	Selection
Q3. What is Supervised Learning?

Supervised Learning is a Machine Learning technique where the model learns from labeled data (features + labels).

Q4. What is Unsupervised Learning?

Unsupervised Learning is a Machine Learning technique where the model learns from unlabeled data and discovers hidden patterns.

Q5. What is Reinforcement Learning?

Reinforcement Learning is a Machine Learning technique where an agent learns through trial and error using rewards and penalties.

Q6. Give one example of each type.
Supervised → Spam Email Detection
Unsupervised → Customer Segmentation
Reinforcement → Robot Navigation


📒 Day 16 Notes – reduce() Function & Classification vs Regression

90-Day Python + AI/ML Roadmap
Student: Surya Rathore
Day: 16 ✅

🐍 Python Development
🔹 reduce() Function
What is reduce()?

reduce() is a function that combines all elements of an iterable into a single value.

Unlike map() and filter(), reduce() is available in the functools module.

Import
from functools import reduce
Syntax
reduce(function, iterable)

The function passed to reduce() takes two arguments:

lambda x, y: ...
x → Accumulated result
y → Next element in the iterable
🔹 Example 1 – Sum of Numbers
from functools import reduce

numbers = [5, 10, 15, 20]

result = reduce(lambda x, y: x + y, numbers)

print(result)

Output

50

Working:

5 + 10 = 15
15 + 15 = 30
30 + 20 = 50
🔹 Example 2 – Product of Numbers
from functools import reduce

numbers = [2, 3, 5]

result = reduce(lambda x, y: x * y, numbers)

print(result)

Output

30
🔹 Example 3 – Maximum Number
from functools import reduce

numbers = [12, 45, 7, 89, 34]

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print(maximum)

Output

89
🔹 Example 4 – Minimum Number
from functools import reduce

numbers = [12, 45, 7, 89, 34]

minimum = reduce(lambda x, y: x if x < y else y, numbers)

print(minimum)

Output

7
📊 map() vs filter() vs reduce()
Function	Purpose	Output
map()	Transform every element	Iterable
filter()	Select elements satisfying a condition	Iterable
reduce()	Combine all elements	Single Value
💡 When to Use reduce()

Use reduce() when you want to:

Find the sum
Find the product
Find the maximum value
Find the minimum value
Combine all elements into one result
🤖 Machine Learning
🔹 Prediction Problems

Machine Learning prediction problems are mainly of two types:

Prediction
│
├── Classification
└── Regression
1️⃣ Classification
Definition

Classification is a Machine Learning task in which the model predicts a category (class/label).

The output is discrete, not continuous.

Examples
Spam / Not Spam
Cat / Dog
Pass / Fail
Fraud / Genuine
Disease / No Disease
Real-Life Applications
Email Spam Detection
Face Mask Detection
Sentiment Analysis
Disease Detection
Image Classification
2️⃣ Regression
Definition

Regression is a Machine Learning task in which the model predicts a continuous numerical value.

Examples
House Price
Salary
Temperature
Rainfall
Car Mileage
Real-Life Applications
House Price Prediction
Stock Price Estimation
Weather Forecasting
Sales Forecasting
Demand Prediction
📊 Classification vs Regression
Classification	Regression
Predicts Categories	Predicts Numerical Values
Output is Discrete	Output is Continuous
Spam / Not Spam	House Price
Cat / Dog	Salary
Pass / Fail	Temperature
Fraud / Genuine	Rainfall Amount
🔑 Important Terms
Category (Class)

A fixed set of possible outputs.

Examples:

Cat
Dog
Spam
Not Spam
Continuous Value

A numerical value that can take many possible values within a range.

Examples:

₹45,75,000
28.6°C
17.3 km/L
🧠 Easy Trick to Remember

Ask yourself:

Does the output belong to a category?

✅ Yes → Classification

Examples:

Cat / Dog
Pass / Fail
Spam / Not Spam
Is the output a number?

✅ Yes → Regression

Examples:

House Price
Salary
Temperature
🎯 Interview Questions
Q1. What is reduce()?

reduce() combines all elements of an iterable into a single value using a function.

Q2. Why do we import reduce() from functools?

Because reduce() is not a built-in function in Python; it is provided by the functools module.

Q3. What is Classification?

Classification is a Machine Learning task that predicts a category or class label.

Q4. What is Regression?

Regression is a Machine Learning task that predicts a continuous numerical value.

Q5. Difference between Classification and Regression?
Classification	Regression
Predicts classes/categories	Predicts numbers
Discrete output	Continuous output
Q6. Give two examples of each.

Classification

Spam Detection
Pass/Fail Prediction

Regression

House Price Prediction
Salary Prediction


📝 Day 17 Notes
🐍 Python – List Comprehensions
Definition

A List Comprehension is a concise way to create a new list in a single line.

Syntax
[new_item for item in iterable]
With Condition
[new_item for item in iterable if condition]
Examples
# Squares
numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers]

# Lowercase
words = ["AI", "ML"]
lower = [x.lower() for x in words]

# Filter Even Numbers
numbers = [1, 2, 3, 4, 5]
even = [x for x in numbers if x % 2 == 0]
Advantages
Shorter code
More readable
More Pythonic
No need for append()
🤖 Machine Learning
Binary Classification

Definition: Predicts exactly two classes.

Examples

Spam / Not Spam
Pass / Fail
Approved / Rejected
Fraud / Genuine
Multi-class Classification

Definition: Predicts three or more classes.

Examples

Digit Recognition (0–9)
Fruit Classification
Animal Classification
Traffic Sign Recognition
Binary vs Multi-class
Binary	Multi-class
2 classes	3 or more classes
Yes/No	Apple/Mango/Banana
Pass/Fail	Digits 0–9
Spam/Not Spam	Traffic Signs
🎯 Interview Questions

Q1. What is a List Comprehension?
A concise way to create a list in a single line.

Q2. What is Binary Classification?
A classification task with exactly two possible classes.

Q3. What is Multi-class Classification?
A classification task with three or more possible classes.

Q4. Difference between Binary and Multi-class Classification?

Binary → 2 classes
Multi-class → 3 or more classes


📒 Day 18 Notes – Dictionary Comprehensions & Logistic Regression
🐍 Python
Dictionary Comprehension
Definition

A Dictionary Comprehension is a concise way to create a dictionary in a single line.

Syntax
{key: value for item in iterable}
Example 1
numbers = [1,2,3,4]

result = {x:x**2 for x in numbers}

print(result)

Output

{1:1,2:4,3:9,4:16}
Example 2
words = ["apple","banana","kiwi"]

result = {word:len(word) for word in words}

Output

{
"apple":5,
"banana":6,
"kiwi":4
}
Example 3 (With Condition)
numbers = [1,2,3,4,5]

result = {x:x**3 for x in numbers if x%2==1}

Output

{
1:1,
3:27,
5:125
}
📊 List vs Dictionary Comprehension
List Comprehension	Dictionary Comprehension
Creates Lists	Creates Dictionaries
[x**2 for x in numbers]	{x:x**2 for x in numbers}
🤖 Machine Learning
Logistic Regression
Definition

Logistic Regression is a Supervised Machine Learning algorithm used for Classification, especially Binary Classification.

Why is it called Regression?

Although the name contains Regression, it does not predict continuous values.

Instead:

Input Features
       ↓
Calculates Probability (0–1)
       ↓
Uses Threshold (0.5)
       ↓
Predicts Class
Example

Spam Detection

Probability = 0.91

0.91 > 0.5

Output = Spam

Another email

Probability = 0.18

0.18 < 0.5

Output = Not Spam
Where is Logistic Regression Used?
📧 Spam Detection
🏦 Loan Approval
❤️ Disease Prediction
💳 Fraud Detection
🛒 Customer Purchase Prediction
📉 Customer Churn Prediction
Linear Regression vs Logistic Regression
Linear Regression	Logistic Regression
Predicts Numbers	Predicts Categories
Used for Regression	Used for Classification
Example: House Price	Example: Spam Detection
Key Terms
Probability

A value between 0 and 1 that represents how likely an event is.

Examples:

0.95 → Very likely
0.50 → Uncertain
0.10 → Very unlikely
Threshold

A cutoff value (commonly 0.5) used to convert probability into a class.

Probability ≥ 0.5 → Positive Class
Probability < 0.5 → Negative Class
🎯 Interview Questions
Q1. What is Logistic Regression?

A supervised learning algorithm used for classification, especially binary classification.

Q2. Why is Logistic Regression called Regression if it performs Classification?

Because it first predicts a probability using a regression equation and then converts that probability into a class label using a threshold.

Q3. What does Logistic Regression predict first?

Probability (0 to 1).

Q4. Give three real-life applications.
Spam Detection
Loan Approval
Disease Prediction

Day 19 Notes
🐍 Python – Set Comprehensions
Definition

A Set Comprehension is a concise way to create a set in a single line.

Syntax
{expression for item in iterable}
Example 1
numbers = [1,2,2,3]

result = {x for x in numbers}

print(result)

Output:

{1, 2, 3}
Example 2
numbers = [1,2,3,4]

result = {x**2 for x in numbers}

print(result)

Output:

{1, 4, 9, 16}
Example 3 (With Condition)
numbers = [1,2,3,4,5,6]

result = {x**3 for x in numbers if x % 2 == 0}

print(result)

Output:

{8, 64, 216}
📊 Comparison
Comprehension	Creates
List	List
Dictionary	Dictionary
Set	Set
🤖 Machine Learning – Sigmoid Function
Why do we need it?

Logistic Regression first computes a value that can be any real number.

The Sigmoid Function converts that value into a probability between 0 and 1.

Any Number
      │
      ▼
Sigmoid Function
      │
      ▼
Probability (0–1)
Important Properties
Output is always between 0 and 1
Large positive input → Output close to 1
Large negative input → Output close to 0
Input = 0 → Output = 0.5
Examples
Input	Output (Approx.)
100	1.00
10	0.999
0	0.5
-10	0.00004
-100	0.00
Logistic Regression Workflow
Input Features
       │
       ▼
Linear Combination
       │
       ▼
Sigmoid Function
       │
       ▼
Probability (0–1)
       │
       ▼
Threshold (0.5)
       │
       ▼
Final Class
🎯 Interview Questions
Q1. What is a Set Comprehension?

A concise way to create a set in a single line.

Q2. Why are sets useful?

They automatically remove duplicate values.

Q3. What is the purpose of the Sigmoid Function?

It converts any real number into a probability between 0 and 1.

Q4. What is the output of Sigmoid(0)?

0.5

Q5. Why is the Sigmoid Function used in Logistic Regression?

Because Logistic Regression needs probabilities between 0 and 1 before making a classification.

📝 Day 20 Notes
🐍 Python – Generator Expressions
Definition

A Generator Expression creates values one at a time (lazily) instead of storing all values in memory.

Syntax
(expression for item in iterable)
Example 1
squares = (x**2 for x in range(5))

print(list(squares))

Output:

[0, 1, 4, 9, 16]
Example 2
words = (word.upper() for word in ["AI", "Python", "ML"])

print(list(words))

Output:

['AI', 'PYTHON', 'ML']
Example 3 (With Condition)
even = (x for x in range(1,11) if x % 2 == 0)

print(list(even))

Output:

[2, 4, 6, 8, 10]
Using next()
cubes = (x**3 for x in range(1,6))

print(next(cubes))
print(next(cubes))
print(next(cubes))

Output:

1
8
27
List vs Generator
List Comprehension	Generator Expression
Uses []	Uses ()
Stores all values immediately	Generates values on demand
Higher memory usage	Lower memory usage
Best for small/medium data	Best for large datasets
🤖 Machine Learning – Decision Boundary
Definition

A Decision Boundary is a boundary that separates different classes predicted by a classification model.

Example

Age vs Laptop Purchase

20   22   25 | 30 | 35   40   45
 No   No   No |    | Yes  Yes  Yes

The line at 30 is the Decision Boundary.

Logistic Regression Workflow
Input Features
      │
      ▼
Linear Combination
      │
      ▼
Sigmoid Function
      │
      ▼
Probability (0–1)
      │
      ▼
Decision Boundary (Threshold = 0.5)
      │
      ▼
Final Class
Decision Rule
Probability ≥ 0.5
        ↓
Positive Class

Probability < 0.5
        ↓
Negative Class
Real-Life Applications
📧 Spam Detection
💳 Fraud Detection
🏦 Loan Approval
❤️ Disease Prediction
📉 Customer Churn Prediction
🎯 Interview Questions
Q1. What is a Generator Expression?

A memory-efficient way to generate values one at a time using parentheses ().

Q2. What is the advantage of a Generator?

It uses less memory because values are generated only when needed.

Q3. What is a Decision Boundary?

A boundary that separates different classes in a classification problem.

Q4. What happens if the predicted probability is 0.82?

Since 0.82 ≥ 0.5, the model predicts the Positive Class.

Q5. What happens if the predicted probability is 0.35?

Since 0.35 < 0.5, the model predicts the Negative Class.


📝 Day 21 Notes
🐍 Python – any() and all()
any()

Returns True if at least one element is True.

Example
numbers = [False, False, True]

print(any(numbers))

Output:

True
all()

Returns True only if every element is True.

Example
numbers = [True, True, False]

print(all(numbers))

Output:

False
Practical Usage
numbers = [2,4,6,7]

print(any(x % 2 == 1 for x in numbers))

Output:

True
marks = [85,92,78,88]

print(all(x > 70 for x in marks))

Output:

True
Memory Trick
any() → At least ONE True

all() → EVERY value must be True
🤖 Machine Learning – Confusion Matrix

A Confusion Matrix evaluates the performance of a classification model.

Actual	Predicted	Name
Positive	Positive	True Positive (TP)
Negative	Negative	True Negative (TN)
Negative	Positive	False Positive (FP)
Positive	Negative	False Negative (FN)
Meanings
✅ True Positive (TP)

Actual = Positive
Predicted = Positive

Correct positive prediction.

✅ True Negative (TN)

Actual = Negative
Predicted = Negative

Correct negative prediction.

❌ False Positive (FP)

Actual = Negative
Predicted = Positive

Also called a False Alarm.

Example:

A genuine email is marked as spam.

❌ False Negative (FN)

Actual = Positive
Predicted = Negative

Also called a Missed Detection.

Example:

A spam email reaches your inbox.

Memory Trick
TP → Correct Positive ✅

TN → Correct Negative ✅

FP → False Alarm 🚨

FN → Missed Detection ❌
🎯 Interview Questions
Q1. What does any() do?

Returns True if at least one element is True.

Q2. What does all() do?

Returns True only if all elements are True.

Q3. What is a Confusion Matrix?

A table used to evaluate the performance of a classification model.

Q4. What is a False Positive?

A negative sample incorrectly predicted as positive.

Q5. What is a False Negative?

A positive sample incorrectly predicted as negative.

Q6. Why are False Negatives often more dangerous?

Because dangerous positive cases (e.g., spam, fraud, disease) are incorrectly classified as safe, allowing them to go undetected.

📝 Day 22 Notes
🐍 Python – zip()
Purpose

zip() combines two or more iterables element by element.

Example
names = ["Surya", "Rahul", "Aman"]
marks = [90, 85, 95]

print(list(zip(names, marks)))

Output:

[('Surya', 90), ('Rahul', 85), ('Aman', 95)]
Memory Trick

Zip a jacket → joins two sides together.

Similarly, zip() joins multiple iterables.

🐍 Python – enumerate()
Purpose

enumerate() adds an index while iterating.

Example
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

Output:

0 Apple
1 Banana
2 Mango
Starting from 1
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

Output:

1 Apple
2 Banana
3 Mango
🤖 Machine Learning – Accuracy
Definition

Accuracy is the percentage of predictions that the model gets correct.

Formula
Accuracy=
TP+TN+FP+FN
TP+TN
	​


Where:

TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative
Example

If:

TP = 30
TN = 50
FP = 10
FN = 10

Then:

Accuracy = (30 + 50) / (30 + 50 + 10 + 10)

= 80 / 100

= 80%

⚠️ Limitation of Accuracy

Accuracy is not reliable for imbalanced datasets.

Example:

990 Healthy
10 Sick

Predicting everyone as Healthy gives 99% accuracy, but misses every sick patient.

Therefore, high accuracy does not always mean a good model.

🎯 Interview Questions
What does zip() do?
What does enumerate() do?
How do you start enumerate() from 1?
What is Accuracy?
Write the Accuracy formula.
Can a model with 99% accuracy still be bad? Why?
Why is Accuracy not suitable for imbalanced datasets?

📝 Day 23 Notes
🐍 Python – Iterators
Definition

An iterator is an object that allows you to traverse a collection one element at a time.

Functions
it = iter(numbers)
next(it)
iter() → Creates an iterator.
next() → Returns the next element.
Raises StopIteration when no elements remain.
🐍 Generators
Generator Expression
gen = (x*x for x in range(1,6))

Uses () instead of [].

Generates values only when needed, making it memory efficient.

Generator Function
def even():
    yield 2
    yield 4
    yield 6
Uses yield.
Pauses execution and resumes from where it left off.
Produces values lazily.
🔄 return vs yield
return	yield
Ends the function	Pauses the function
Returns one value	Produces multiple values over time
Doesn't remember state	Remembers state
🤖 Machine Learning – Precision
Definition

Precision answers:

Out of all the predictions that the model labeled as Positive, how many were actually Positive?

Formula
Precision=
TP+FP
TP
	​

	​


Where:

TP = True Positive
FP = False Positive
Why Precision Matters

Precision is important when False Positives are costly.

Examples:

📧 Spam Detection
🚨 Fraud Alerts
🔐 Security Systems
📧 Spam Detection Example

Suppose:

Model predicts 100 emails as Spam
90 are actually spam (TP)
10 are genuine emails marked as spam (FP)

Precision:

90+10
90
	​

=90%

A higher precision means fewer important emails are incorrectly marked as spam.

📊 Accuracy vs Precision
Accuracy	Precision
Overall correct predictions	Correctness of positive predictions
Uses TP, TN, FP, FN	Uses TP and FP
Can mislead on imbalanced data	Better when False Positives matter
🎯 Interview Questions
What is an iterator?
What is the difference between iter() and next()?
What is a generator?
Difference between yield and return.
Why are generators memory efficient?
Write the formula for Precision.
When should Precision be preferred over Accuracy?
Why is Precision important in spam detection?

