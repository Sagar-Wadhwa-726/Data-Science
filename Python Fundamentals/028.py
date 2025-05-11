# Without walrus operator
# while True:
#     line = input("Enter an input : ")
#     if line=="":
#         break
#     else:
#         print(f"You enetered {line}")
        
        
# With walrus operator
# This operator can be used to assign a value to a variable as part of an expression.
while (line := input("Enter an input : ") != ""):
    if line=="":
        break
    else:
        print(f"You enetered {line}")      