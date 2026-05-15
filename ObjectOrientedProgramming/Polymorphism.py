# Means many forms in Greek, In OOPs , Polymorphism allows objects of different classes as if they are the object of the same class & It enables reusability and makes Programs more flexible,



# Types of Polymorphism:
# Method Overriding  (Runtime Polymorphism)
# Method Overloading (Compile Time Polymorphism)
# Operator Overloading (Compile Time Polymorphism)



# Method Overriding ---> A child class provides a specific implementation
# of method that has already been defined into the parent class. this allow Dynamic selection at runtime 



from curses.textpad import rectangle


class Grandparent: # parent class
    def speak(self):
        print("Hello my name is Amit")
    

class Parent(Grandparent) : #child class
    

    def speak(self):
        print("Hello my name is junior amit")
        
        
class Child(Grandparent):
    def speak(self):
        print("Hello my junior amit junior")
        
        
def attribute_provider(objects):
    print(objects.speak())

grands=Grandparent()

# print(attribute_provider(grands))

parent=Parent()


# print(attribute_provider(parent))   
  
  

child=Child()
# print(attribute_provider(child))




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
        
    
    
circle=Circle(4)

circle.area()