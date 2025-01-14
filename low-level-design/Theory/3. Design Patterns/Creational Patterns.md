# Creational Design Patterns

Creational design patterns are a category of design patterns that deal with object creation mechanisms. These patterns aim to abstract the instantiation process, making the system independent of how its objects are created, composed, and represented.

## Singleton Pattern

The Singleton Pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to that instance. The instance is created only when it is needed.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
```

### Terms Used

  
- ```__new__``` -> A special method in Python that is responsible for creating a new instance of a class. 
It is called before the ```__init__``` method, which initializes the instance. It essentially allocates memory in the heap. We are checking if the memory is already allocated, if not allocate it and return

- ```cls``` -> cls is a conventional name for the class itself, used as the first argument in class methods or the ```__new__``` method. It allows access to the class attributes and methods.

- ```self``` is different from ```cls```. ```self``` represents the instance of the class.  ```cls``` is the class itself and not a specific instance. ```self``` is used in instance methods, and ```cls``` 
is used in class methods. ```self``` refers to the attributes and methods of an instance. ```cls``` refers to the class level attributes and methods.

- ```*args``` allows a function or method to accept a variable number of positional arguments. 
It is used when the number of arguments is not known in advance.

    - ##### Example:
    ```python
    def print_all(*args):
        for arg in args:
            print(arg)

    # Usage
    print_all(1, 2, 3, 4)
    ```

- ```**kwargs``` allows a function or method to accept a variable number of keyword arguments. It is used when the number of named arguments is not known in advance.

    - ##### Example
    ```python
    def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    # Usage
    print_all(name="Alice", age=25, city="New York")
    ```

### Thread Safe Singleton

```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()  # Lock for thread safety

    def __new__(cls, *args, **kwargs):
        with cls._lock:  # Ensure that only one thread can create the instance
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
```

## Prototype Pattern

The Prototype Design Pattern is a creational design pattern that allows you to create new objects by copying existing ones (prototypes). This approach avoids the cost and complexity of creating objects from scratch and provides a mechanism to duplicate objects while preserving their state.

```python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)  # Creates a deep copy of the object

class Document(Prototype):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Document(title={self.title}, content={self.content})"
```

## Builder Pattern

The Builder Design Pattern is a creational design pattern used to construct complex objects step by step. It separates the construction process from the representation, allowing the same construction process to create different representations of the object.

```python
class Computer:
    """Product class representing the complex object."""
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, gpu={self.gpu}, ram={self.ram}, storage={self.storage})"

class ComputerBuilder:
    """Builder interface defining the steps to build a computer."""
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer
```

### Director in Builder Pattern

In some implementations, a Director class is introduced to manage the construction process and ensure the product is built in a consistent manner. The Director orchestrates the order and logic of the building steps.


```python
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_gaming_pc(self):
        return (self.builder.set_cpu("Intel i9")
                          .set_gpu("NVIDIA RTX 4090")
                          .set_ram("32GB")
                          .set_storage("2TB SSD")
                          .build())

    def construct_office_pc(self):
        return (self.builder.set_cpu("Intel i5")
                          .set_gpu("Integrated")
                          .set_ram("8GB")
                          .set_storage("512GB SSD")
                          .build())
```

## Factory Pattern


The Factory Design Pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. This pattern promotes loose coupling between client code and the classes it instantiates.


```python
from abc import ABC, abstractmethod

# Step 1: Define an interface for the product
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Concrete implementations of the product
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

# Step 3: Factory Method
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Client code
circle = ShapeFactory.create_shape("Circle")
print(circle.draw())  # Output: Drawing a Circle

square = ShapeFactory.create_shape("Square")
print(square.draw())  # Output: Drawing a Square
```

## Abstract Factory Pattern


The Abstract Factory Design Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is particularly useful when a system needs to support multiple configurations or environments.


```python
from abc import ABC, abstractmethod

# Step 1: Abstract Product Interfaces
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Step 2: Concrete Products
class WinButton(Button):
    def render(self):
        return "Rendering Windows Button"

class MacButton(Button):
    def render(self):
        return "Rendering Mac Button"

class WinCheckbox(Checkbox):
    def render(self):
        return "Rendering Windows Checkbox"

class MacCheckbox(Checkbox):
    def render(self):
        return "Rendering Mac Checkbox"

# Step 3: Abstract Factory Interface
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Step 4: Concrete Factories
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# Step 5: Client Code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

# Create Windows UI
win_factory = WinFactory()
print("Windows UI:")
client_code(win_factory)

# Create Mac UI
mac_factory = MacFactory()
print("\nMac UI:")
client_code(mac_factory)
```