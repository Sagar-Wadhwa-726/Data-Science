# If we want to pass the arguments to the function then one more mehtod is required outside the nested method
# Decorators are majorly used for changing the functionality of a function
def repeat(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator


"""

This will be boiled down to somethhing like this:

            for i in range(7):
                say_hello("Sagar")

"""
@repeat(2)
def say_hello(name):
    print(f"Hello {name}")
    
say_hello("Sagar")