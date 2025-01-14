# Structural Design Patterns

Structural design patterns are a category of software design patterns that focus on simplifying the relationships and interactions between different objects in a system. They help ensure that these objects can work together effectively while maintaining flexibility and scalability.

Popular Structural Design Patterns

- Adapter - Allows two incompatible systems to work together (legacy systems)
- Bridge - Decouples abstraction from implementation
- Composite - Provided a tree like hierarchial structure
- Decorator - Allows more features to be wrapped around a class
- Facade - Simplies complex implementations
- Flyweight - Reduces memory consumption by initializing only once
- Proxy - Controls the actual object, features like lazy loading, etc

## Adapter Pattern

The Adapter Pattern is a structural design pattern that allows two incompatible interfaces to work together. It acts as a bridge between the two, translating requests or data so that the client and the target can interact seamlessly.

```python
# The Target interface
class Printer:
    def print(self, text: str):
        raise NotImplementedError("This method should be overridden.")

# The Adaptee (incompatible class)
class LegacyPrinter:
    def print_uppercase(self, text: str):
        print(text.upper())

# The Adapter
class PrinterAdapter(Printer):
    def __init__(self, adaptee: LegacyPrinter):
        self.adaptee = adaptee

    def print(self, text: str):
        # Adapter translates the request
        self.adaptee.print_uppercase(text)

# Client code
def client_code(printer: Printer):
    printer.print("Hello, Adapter Pattern!")

# Usage
legacy_printer = LegacyPrinter()
adapter = PrinterAdapter(legacy_printer)

# Client can now use the adapter as if it's the expected interface
client_code(adapter)
```

## Bridge Pattern

The Bridge Pattern is a structural design pattern that decouples an abstraction from its implementation, allowing the two to evolve independently. It is particularly useful when a class has multiple orthogonal dimensions of variation.

```python
# Implementor
class Renderer:
    def render_circle(self, radius: float):
        raise NotImplementedError("This method should be implemented by subclasses.")

# ConcreteImplementor 1
class VectorRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f"Drawing a circle with radius {radius} as vectors.")

# ConcreteImplementor 2
class RasterRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f"Drawing a circle with radius {radius} as pixels.")

# Abstraction
class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

# RefinedAbstraction
class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor

# Client code
def client_code():
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle = Circle(vector_renderer, 5)
    circle.draw()

    circle.resize(2)
    circle.draw()

    circle = Circle(raster_renderer, 3)
    circle.draw()

# Run client code
client_code()

```

## Composite Design Pattern

The Composite Pattern is a structural design pattern that allows you to compose objects into tree structures to represent part-whole hierarchies. It enables you to treat individual objects and groups of objects uniformly.


```python
# Component
class FileSystemComponent:
    def show_details(self, indent: int = 0):
        raise NotImplementedError("This method should be implemented by subclasses.")

# Leaf
class File(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name

    def show_details(self, indent: int = 0):
        print(" " * indent + f"File: {self.name}")

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_details(self, indent: int = 0):
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.show_details(indent + 2)

# Client code
def client_code():
    # Leaf nodes
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    # Composite nodes
    sub_directory = Directory("SubDir")
    sub_directory.add(file1)
    sub_directory.add(file2)

    root_directory = Directory("Root")
    root_directory.add(sub_directory)
    root_directory.add(file3)

    # Display the file system structure
    root_directory.show_details()

# Run client code
client_code()

```

## Decorator Pattenr

The Decorator Pattern is a structural design pattern that allows you to dynamically add behavior or responsibilities to an object without modifying its code. It wraps the original object, providing additional functionality while maintaining the same interface.

```python
# Component
class Text:
    def render(self) -> str:
        raise NotImplementedError("This method should be implemented by subclasses.")

# ConcreteComponent
class PlainText(Text):
    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return self.content

# Decorator
class TextDecorator(Text):
    def __init__(self, wrapped: Text):
        self.wrapped = wrapped

    def render(self) -> str:
        return self.wrapped.render()

# ConcreteDecorator 1
class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"<b>{super().render()}</b>"

# ConcreteDecorator 2
class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"<i>{super().render()}</i>"

# Client code
def client_code():
    plain = PlainText("Hello, Decorator Pattern!")

    bold = BoldDecorator(plain)
    italic = ItalicDecorator(plain)
    bold_italic = ItalicDecorator(bold)

    print("Plain Text: ", plain.render())
    print("Bold Text: ", bold.render())
    print("Italic Text: ", italic.render())
    print("Bold + Italic Text: ", bold_italic.render())

# Run client code
client_code()

```

## Facade Pattern

The Facade Pattern is a structural design pattern that provides a simplified interface to a complex subsystem. It hides the complexity of the subsystem by exposing a single, unified interface for the client to interact with.

```python
# Subsystem 1
class DVDPlayer:
    def on(self):
        print("DVD Player is ON.")
    
    def play(self, movie: str):
        print(f"Playing movie: {movie}")
    
    def off(self):
        print("DVD Player is OFF.")

# Subsystem 2
class Amplifier:
    def on(self):
        print("Amplifier is ON.")
    
    def set_volume(self, level: int):
        print(f"Volume set to {level}.")
    
    def off(self):
        print("Amplifier is OFF.")

# Subsystem 3
class Projector:
    def on(self):
        print("Projector is ON.")
    
    def set_input(self, input_source: str):
        print(f"Projector input set to {input_source}.")
    
    def off(self):
        print("Projector is OFF.")

# Subsystem 4
class Lights:
    def dim(self):
        print("Lights are dimmed.")
    
    def on(self):
        print("Lights are ON.")

# Facade
class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, amp: Amplifier, projector: Projector, lights: Lights):
        self.dvd = dvd
        self.amp = amp
        self.projector = projector
        self.lights = lights

    def watch_movie(self, movie: str):
        print("Starting home theater system...")
        self.lights.dim()
        self.projector.on()
        self.projector.set_input("DVD")
        self.amp.on()
        self.amp.set_volume(10)
        self.dvd.on()
        self.dvd.play(movie)
        print("Movie started. Enjoy!")

    def end_movie(self):
        print("Shutting down home theater system...")
        self.dvd.off()
        self.amp.off()
        self.projector.off()
        self.lights.on()
        print("Home theater system is OFF.")

# Client code
def client_code():
    # Subsystem components
    dvd = DVDPlayer()
    amp = Amplifier()
    projector = Projector()
    lights = Lights()

    # Facade
    home_theater = HomeTheaterFacade(dvd, amp, projector, lights)

    # Client interacts only with the facade
    home_theater.watch_movie("Inception")
    print()
    home_theater.end_movie()

# Run client code
client_code()
```

## Flyweight Pattern

The Flyweight Pattern is a structural design pattern that focuses on minimizing memory usage by sharing as much data as possible with similar objects. It is useful when you need to create a large number of objects that share some common state.

```python
# Flyweight
class Character:
    def __init__(self, char: str, font: str):
        self.char = char  # Intrinsic state
        self.font = font  # Intrinsic state

    def display(self, x: int, y: int):
        # Extrinsic state: x and y position
        print(f"Character: {self.char}, Font: {self.font}, Position: ({x}, {y})")

# FlyweightFactory
class CharacterFactory:
    def __init__(self):
        self.characters = {}

    def get_character(self, char: str, font: str):
        key = (char, font)
        if key not in self.characters:
            self.characters[key] = Character(char, font)
            print(f"Created new Flyweight for: {key}")
        else:
            print(f"Reused existing Flyweight for: {key}")
        return self.characters[key]

# Client
def client_code():
    factory = CharacterFactory()

    # Create characters
    c1 = factory.get_character('a', 'Arial')
    c2 = factory.get_character('b', 'Arial')
    c3 = factory.get_character('a', 'Arial')  # Reuses existing Flyweight
    c4 = factory.get_character('a', 'Times New Roman')

    # Display characters with extrinsic state
    c1.display(10, 20)
    c2.display(30, 40)
    c3.display(50, 60)  # Shares intrinsic state with c1
    c4.display(70, 80)

# Run client code
client_code()

```

## Proxy Design Pattern

The Proxy Pattern is a structural design pattern that provides a placeholder or surrogate for another object to control access to it. The proxy controls the interaction with the real object, allowing additional functionality such as lazy initialization, access control, or logging.

```python
# Subject
class Image:
    def display(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

# RealSubject
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None  # RealImage is initialized lazily

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)  # Load RealImage only when needed
        self.real_image.display()

# Client code
def client_code():
    # Proxy object
    image = ProxyImage("example.jpg")

    # Image is not loaded yet
    print("Image object created, but not loaded.")

    # First access to the image
    image.display()

    # Second access to the image (already loaded)
    image.display()

# Run client code
client_code()

```