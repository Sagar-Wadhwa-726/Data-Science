# A set is a collection of unique elements, duplicates are not there
# Sets are unordered, every element is stored at some random order

my_set = {1,2,3,3,3}
my_set.add(33)
my_set.add(4356)
my_set.add(443)
my_set.add(46)
my_set.add(1907)

print(my_set)

# remove method -> if element not present throws error
# discard method -> if element is not present does not throws error

my_set.discard(33)
my_set.pop()
my_set.pop()
print(my_set)

my_frozen_set = frozenset([1,2,3,4])
print(my_frozen_set)
my_frozen_set.add(2)