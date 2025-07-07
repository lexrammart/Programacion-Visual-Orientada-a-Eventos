from Figura2D import Figura2D

class Rectangulo(Figura2D):
    def __init__(self,color, base, altura):
        super().__init__(color)
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base
    
    @property
    def altura(self):
        return self.__altura
     
    @base.setter
    def base(self, base):
        self.__base = base

    @altura.setter
    def altura(self, altura):
        self.__altura = altura    

    def calcularArea(self):
        return self.altura * self.base 

    def __str__(self):
        return (super().__str__() + 
                f"Áltura: {self.altura}" +
                f"\nBase: {self.base}" +
                f"\nÁrea: {self.calcularArea()}")
