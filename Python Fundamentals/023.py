class Employee():
    company = "HP"
    
    # Instance method
    def __init__(self, name, salary):       
        self.name = name
        self.salary = salary
    
    # Instance method
    def print_Employee_info(self):
        print(f"The name is {self.name} & salary is Rs.{self.salary}")
        
    # Static method
    @staticmethod
    def sum_numbers(a, b):
        return a+b
    
    # Class method 
    @classmethod
    def print_info_class(cls):
        return cls.company
    
    @classmethod
    def change_company(cls, new_company):
        cls.company=new_company


e = Employee("Sagar",80000)
e.print_Employee_info()
print(e.sum_numbers(10,10))
print(Employee.print_info_class())

print(Employee.company)
Employee.change_company("Acer")
print(Employee.company)



