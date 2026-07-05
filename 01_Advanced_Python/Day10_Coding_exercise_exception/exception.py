try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    elif age > 120:
        raise ValueError("Invalid age entered.")

except ValueError as e:
    print(e)

else:
    print("Age accepted.")

    if age >= 18:
        print("Eligible for voting.")
    else:
        print("Not eligible for voting.")

finally:
    print("Program Finished.")
    