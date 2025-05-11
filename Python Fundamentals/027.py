from functools import reduce
"""These are higher order functions in python, these operate over iterables, help us to perform common set of operation over the items of the iterable"""
#  Map
numbers = [1,2,3,4];

'''Creating a new list where all the elements are the square of the original numbers list'''
square_list = list(map(lambda x : x*x,numbers))
print(square_list)

# Filter
a = [-1,-2,-3,0,1,2,3,4]

new_a = list(filter(lambda x : x>0, a))
print(new_a)    

# Reduce

def add_numbers(a,b):
    return a+b

a=[1,2,3]

'''Reduce can be used to reduce an iterable into a single number'''

print(reduce(add_numbers, a, 0))



