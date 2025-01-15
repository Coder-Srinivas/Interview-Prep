from abc import ABC, abstractmethod
from typing import List

class Log(ABC):

    @ abstractmethod
    def log(self, message:str, severity:int, history: List[str]):
        pass