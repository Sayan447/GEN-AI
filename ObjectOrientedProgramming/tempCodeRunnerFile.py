class Shape:
    def area(self):
        return "this method returns the area of the shape"
    
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
        return self.width*self.height
    
    
    class Circle(Shape):
        def __init__(self,radius):
            self.radius=radius
            
        def area(self):
            3.14 * self.radius * self.radius
            
            
shape=Shape()
print(shape.area())
        






rectangle=Rectangle(6,4)
print(rectangle.area())
        