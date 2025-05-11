# Tuples are very similar to lists in python, just the difference is that tuple is immutable

# to create a tuple with one element use comma

tuple_1 = (1,2,3,4,5)
print(tuple_1)

tuple_2 = (4,)
print(tuple_2)

tuple_3 = ()
print(tuple_3)

# tuple unpacking 
tu = (1,2,3)
a,b,c = tu
print(a,b,c)

tu_another = (1,1,1,1,1,1,2,3,45,6,7,5,5,5,5,5,5)
print(tu_another.count(1))

print(tu_another.index(45))