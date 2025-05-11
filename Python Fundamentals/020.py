# A decorator is a function that takes a function, creates a new function (decorator) and then this function
def decorator(func):
    def wrapper():
        print("I am about to execute this function !")
        func()
        print("I have executed this function !")
    return wrapper

def say_hello():
        print("Hello")


""" f function will look exactly like this under the hood
def f():
    print("I am about to execute this function !")
    print("Hello")
    print("I have executed this function !")

"""
f=decorator(say_hello)
f()

# decorators can be used to chane the functionality of the existing functions
# We can alos define the decorators using below syntax
@decorator
def say_bye():
    print("Bye bye bye bye !!")

say_bye()