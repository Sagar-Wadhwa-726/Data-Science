# Else - this block will be executed if no exception is caught
# Finally - this block will be executed even if the exception is caught or not
try:
    a=345/10
except Exception as e:
    print(e)

else:
    print("Else block will be executed only if the error is not thrown !")

finally:
    print("Finally block will be executed no matter if the exception is thrown or not !")
    
'''But instead of finally we can have a simple print statement also - then why do we need finally keyword ? This keyword is helpful when we have exception handling code written inside of a function. This will make sure that even if the function returns irrespective of the fact whether an exception is thrown or not, the finally block will be executed even if the fucntion returns. This is useful for the cases where we want some cleanup to happen.'''

