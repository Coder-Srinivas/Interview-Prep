from log import Log

class InfoLogger(Log):

    def __init__(self, successor=None):
        self.successor = successor
        self.severity = 1

    def log(self, message, severity, history):
        if self.severity == severity:
            history.append(message)
            print(message)
        elif self.successor:
            self.successor.log(message, severity, history)
        else:
            history.append(f"Cannot handle \033[91m{severity}\033[0m")
            raise NotImplementedError(f"Cannot handle {severity}")
        