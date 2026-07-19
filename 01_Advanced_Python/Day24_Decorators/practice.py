def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@decorator
def hello():
    print("Hello Surya!")

hello()

def decorator(func):
    def wrapper():
        print("Starting...")
        func()
    return wrapper

@decorator
def study():
    print("Learning AI")
study()