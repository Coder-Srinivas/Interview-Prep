from log import Log

class DebugLogger(Log):

    def __init__(self, successor=None):
        self.successor = successor
        self.severity = 2

    def log(self, message, severity, history):
        if self.severity == severity:
            modified_message = f"\033[93m{message}\033[0m"
            print(modified_message)
            history.append(modified_message)
        elif self.successor:
            self.successor.log(message, severity, history)
        else:
            history.append(f"Cannot handle \033[91m{severity}\033[0m")
            raise NotImplementedError(f"Cannot handle {severity}")
            
        