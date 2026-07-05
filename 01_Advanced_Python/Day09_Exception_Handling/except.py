try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print(x/y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input! please enter numbers only")
else:
    print("Division Successful")
finally:
    print("Program ended")


