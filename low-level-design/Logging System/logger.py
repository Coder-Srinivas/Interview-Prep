from typing import List
import threading

from debug_logger import DebugLogger
from error_logger import ErrorLogger
from info_logger import InfoLogger

class Logger:

    _instance = None
    _lock = threading.Lock()
    error = ErrorLogger()
    debug = DebugLogger(error)
    info = InfoLogger(debug)
    history: List[str] = []

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def log(self, message, severity):
        try:
            self.info.log(message=message, severity=severity, history=self.history)
        except NotImplementedError as error:
            print(error)

    def log_history(self):
        print(self.history)
