class Employee:
    company="HP"
    
    # Constructors can be used to initialize the objects 
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond
        

    def get_details(self):
        print(f"The name is {self.name}")
        print(f"The salary of {self.name} is {self.salary}")
        print(f"The bond is for {self.bond} year(s)")

e1 = Employee(80000,"Sagar",1)
e2 = Employee(50000,"Anmol",10)
e1.get_details()
e2.get_details()

# Object introspection : Tells the methods which can be called on this object along with the attributes
print(dir(e1))
