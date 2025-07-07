from abc import ABC, abstractmethod

class Figura2D(ABC):
    def __init__(self, color):
        self.__color = color

    @property
    def color(self, color):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self): 
        return f"Color de la figura: {self.__color}"