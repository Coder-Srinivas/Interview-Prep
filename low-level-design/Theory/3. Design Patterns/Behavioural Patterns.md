# Behavioural Design Patterns

Behavioral design patterns are a category of software design patterns that focus on the communication and interaction between objects. These patterns help manage complex control flows and reduce coupling, improving the flexibility and maintainability of the system.

Popular Design Patterns

- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor


## Chain of Responsibility

The Chain of Responsibility pattern is a behavioral design pattern that allows a request to be passed along a chain of handlers. Each handler can either process the request or pass it to the next handler in the chain.

This pattern is particularly useful when you want to decouple the sender of a request from its receivers. It avoids tightly coupling components by allowing multiple handlers to process the request dynamically.

Used in ATM/Vending Machine

```python
class Handler:
    """
    Abstract handler that defines the interface for processing requests.
    """
    def __init__(self, successor=None):
        self.successor = successor  # Next handler in the chain

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)
        return None


class SpamHandler(Handler):
    def handle(self, request):
        if "spam" in request:
            return f"SpamHandler processed the request: {request}"
        return super().handle(request)


class FanHandler(Handler):
    def handle(self, request):
        if "fan" in request:
            return f"FanHandler processed the request: {request}"
        return super().handle(request)


class ComplaintHandler(Handler):
    def handle(self, request):
        if "complaint" in request:
            return f"ComplaintHandler processed the request: {request}"
        return super().handle(request)


# Setting up the chain of handlers
complaint_handler = ComplaintHandler()
fan_handler = FanHandler(complaint_handler)
spam_handler = SpamHandler(fan_handler)

# Client code
requests = ["spam email", "fan message", "complaint about service", "general inquiry"]

for req in requests:
    result = spam_handler.handle(req)
    if result:
        print(result)
    else:
        print(f"No handler could process the request: {req}")

```

## State

The State Pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. It encapsulates state-specific behavior within separate classes, enabling the object to delegate behavior to the current state instead of implementing state transitions in its own logic.

```python
from abc import ABC, abstractmethod

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, context):
        pass


# Concrete States
class RedLight(TrafficLightState):
    def handle(self, context):
        print("Red Light: Stop!")
        context.set_state(GreenLight())


class GreenLight(TrafficLightState):
    def handle(self, context):
        print("Green Light: Go!")
        context.set_state(YellowLight())


class YellowLight(TrafficLightState):
    def handle(self, context):
        print("Yellow Light: Slow down!")
        context.set_state(RedLight())


# Context
class TrafficLight:
    def __init__(self):
        self.current_state = RedLight()  # Initial state

    def set_state(self, state):
        self.current_state = state

    def change(self):
        self.current_state.handle(self)


# Client Code
if __name__ == "__main__":
    traffic_light = TrafficLight()

    # Simulate traffic light cycles
    for _ in range(6):  # Cycle through the states twice
        traffic_light.change()
```

