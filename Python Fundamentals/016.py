class Employee:
    # Class Attribute
    company="HP"
    
    # self referes to the current object on which the method is called
    # it is similar to this keyword in c++
    def get_salary(self):
        print(f"The salary of {self} is 80000")

e1 = Employee()
e2 = Employee()
e1.get_salary()
e2.get_salary()
