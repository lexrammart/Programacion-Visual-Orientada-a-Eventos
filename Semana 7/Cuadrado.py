from Figura2D import Figura2D

class Cuadrado(Figura2D):
    
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado
    
    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, lado):
        self.__lado = lado
    
    def calcularArea(self):
        return self.__lado * self.__lado

    # @property
    # def color(self):
    #     return self.__color 

    # @color.setter
    # def color(self, color):
    #     self.__color = color

    def __str__(self):
        return super().__str__() + f"\nLado: {self.__lado}\nÁrea: {self.calcularArea()}\n"