**Classes in Python**  

Classes provide a means of bundling data and functionality together. Creating a 
new class creates a new type of object, allowing new instances of that type to be 
made.

Attributes of a class can be created at class level or instance level:

**class level:**
* class level attributes are variables that are inherited by every object of the class: they are shared across every object of the class
* value of the class attributes remains the same for every new object of the class
* they are defined outside the `__init__()` function, and placed at the top

**instance level:**
* instance level attributes are unique to the specific object
* different values can be defined for each object of a class with the `__init__()` function
* instance attributes are placed below the `__init__()` function and that is always under the class attributes.

**Class and instance variables**  
```py
class Dog:
    kind = 'canine' # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance
        
    def add_trick(self, trick):
        self.tricks.append(trick)  #this is appended to the instance, NOT the class

d = Dog('Fido')
e = Dog('Buddy')
d.kind  #returns canine
e.kind  #returns canine
d.name  #returns Fido
e.name  #returns Buddy
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks #returns only 'roll over' because that is assigned to d only
```

**Inheritance**  
A base class can be added when a class object is constructed, example:  
```py
class Dog(AnimalClass):
    kind = 'canine' # class variable shared by all instances
```
If a requested attribute is not found in the class, the search will look into the base class for that attribute. The derived class can extend or override the base class methods.

The 'self' keyword represents the instance of the class: it works as a **handle for accessing the data members like attributes** from the class methods.

The `__init__()` is called automatically by Python for every object created from the class. **It's purpose is to initialize the object attributes with values that are supplied by the user**. It is known as Constructor in OOP.

The class inheritance mechanism allows multiple base classes. A derived class 
can override any methods of its base class or classes, and a method can call 
the method of a base class with the same name.

The simplest form of class definition looks like this:
```py
class ClassName:
    <statement-1>
    .
    .
    <statement-N>
```
Class definitions, like function definitions (def statements) must be executed 
before they have any effect.
```py
class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        return 'hello world'

MyClass.i # return the int
MyClass.f # returns a function object
MyClass.__doc__ # magic method/dunder method that return the text literal

x = MyClass() #instantiates the class
x.i # return the int
x.f() # calls the class method
```

**Add or delete an attribute**  
Add a data attribute and assign a value:  
```py
x.counter = 1
while x.counter < 10:
  x.counter = x.counter * 2

print(x.counter)  #returns 16 as last value: it is bigger than 10 so the loop stops

del x.counter  #this removes the attribute completely
```

**Python super()**  
Calling super() gives access to methods in a superclass from the subclass that inherits from it. Using super() alone returns a temporary object of the superclass that then allows you to call that superclass’s methods. A common use case is building classes that extend the functionality of previously built classes.

Example with similar objects:
```py
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
```
Some code is duplicated because the classes have similar attributes. Using `super()` the code is simplified:
```py
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```
In this example, Rectangle is the superclass, and Square is the subclass. Using `super()` allows you to call methods of the superclass in your subclass. The primary use case of this is to extend the functionality of the inherited method.

Now we can create a class Cube that inherits from Square and extends the functionality of .area() (inherited from the Rectangle class through Square):
```py
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length
```
**Important:** `super()` has to be called in the Cube class to access the methods inherited from the superclass Rectangle.