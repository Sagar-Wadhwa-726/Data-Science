# # Strings are immutable in python, once a string is created we can't modify the strings
# name = "Sagar"
# print(name)
# # name[0]="d" will throw runtime error
# print(name)

# para = "this is a line which will be shown as a paragraph"
# print(para.capitalize())
# print(para.title())

para = "Apple,Banana,Mango"
listt=para.split(",")
print(listt)
print(",".join(listt))