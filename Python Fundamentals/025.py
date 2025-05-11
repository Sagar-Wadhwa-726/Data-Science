while True:
    try:
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        print(f"The sum is : {a+b}")
        
    # The program will not crash here, since we have handled/caught the error
    except Exception as e:
        print("Some Error occurred !",e.args)
    