class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def print_point(self):
        print(f"X = {self.x}, Y = {self.y}")
    
    def add_points(self, p):
        return Point((self.x+p.x), (self.y+p.y))
    
    def __add__(self,p):
        return Point((self.x+p.x), (self.y+p.y))

p1 = Point(1,2)
p2 = Point(3,4)
# The + operator is overloaded using the __add__ method to add two points.
p = p1+p2

p.print_point()