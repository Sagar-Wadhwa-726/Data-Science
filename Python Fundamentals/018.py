class Animal:
    location = "India"
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Speaking now . . .")
    
    def print_details(self):
        print(f"The name of the animal is {self.name}")
        
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof !!!")
    

d = Dog("Kinnu")
print(d.location)
d.speak()
d.print_details()