"""
Módulo que define la clase abstracta `Pelota`, base para las diferentes pelotas utilizadas
en el sorteo.

Proporciona los atributos y la interfaz común que comparten las subclases encargadas de
representar pelotas con números o letras.
"""

from abc import ABC, abstractmethod


class Pelota(ABC):
    """
    Clase abstracta que modela una pelota participante en el sorteo.

    Atributos:
        id (int | str): Identificador único de la pelota.
        participante (str): Nombre del participante asociado.
        color (str): Color actual de la pelota. Inicialmente blanco.

    Métodos abstractos:
        pintarPelota(): Cambia el color de la pelota según la lógica de la subclase.
        generarValor(): Genera y asigna el valor propio de la pelota.

    El método ``__str__`` devuelve una representación legible de la instancia.
    """

    def __init__(self, id, participante):
        self.__id = id
        self.__participante = participante
        self._color = "blanco"  # color inicial

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def participante(self):
        return self.__participante

    @property
    def color(self):
        return self._color

    # Setters
    @id.setter
    def id(self, valor):
        self.__id = valor

    @participante.setter
    def participante(self, valor):
        self.__participante = valor

    @color.setter
    def color(self, valor):
        if valor in ["blanco", "azul", "verde", "rojo", "amarillo", "morado", "rosa"]:
            self._color = valor
        else:
            raise ValueError("Color inválido para la pelota.")

    # Métodos abstractos
    @abstractmethod
    def pintarPelota(self):
        """Define cómo se pinta la pelota. Debe implementarse en las subclases."""
        pass

    @abstractmethod
    def generarValor(self):
        """Genera y asigna el valor de la pelota (número o letra). Debe implementarse en las subclases."""
        pass

    @abstractmethod
    def decifrarPremio(self):
        pass

    # Método __str__ base
    def __str__(self):
        """Devuelve una representación de cadena con el ID, participante y color actuales."""
        return f"ID: {self.__id}, Participante: {self.__participante}, Color: {self._color}"
