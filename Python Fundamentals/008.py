def findAverage(a,b,c=0):
    return (a+b+c)/3

print(findAverage(1,1111))

# the above concept covers default and positional arguments
# now let's talk about the keyword arguments

print(findAverage(b=22,a=33,c=22212))