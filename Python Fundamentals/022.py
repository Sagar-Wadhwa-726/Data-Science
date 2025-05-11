class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @property
    def first_name(self):
        return self.name.split(" ")[0]
    
    @first_name.setter
    def first_name(self, new_name):
        self.name = new_name
        
e = Employee("Jack",34555)
# e.projects = 6
# print(e.projects)
# print(e.first_name())
print(e.first_name)
e.first_name="Wadhwa"
print(e.first_name)
        