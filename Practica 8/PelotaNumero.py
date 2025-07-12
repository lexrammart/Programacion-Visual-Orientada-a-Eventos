"""
Módulo que define la clase PelotaNumero, subclase de Pelota para representar
pelotas con valor numérico en el sorteo.

Contiene la lógica para generar un número aleatorio y pintar la pelota con un color.
"""

from Pelota import Pelota
import random as rd


class PelotaNumero(Pelota):
    """
    Subclase de Pelota que representa una pelota cuyo valor es un número.

    Atributos:
        __numero (int): Número asignado a la pelota. Inicialmente 0.

    Métodos:
        generarValor(): Asigna aleatoriamente un número entre 1 y 4.
        pintarPelota(): Cambia el color de la pelota aleatoriamente.
    """

    def __init__(self, id, participante):
        super().__init__(id, participante)
        self.__numero = 0  # valor inicial

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        self.__numero = valor

    # métodos requeridos
    def generarValor(self):
        """Genera y asigna aleatoriamente un número entre 1 y 4."""
        self.__numero = rd.randint(1, 4)

    def pintarPelota(self):
        """Selecciona aleatoriamente un color para la pelota entre 'amarillo', 'morado' o 'rosa'."""
        self.color = rd.choice(["amarillo", "morado", "rosa"])  # usa el setter heredado

    # decifrar premio
    def decifrarPremio(self):
        # return super().decifrarPremio()
        pass

    # toString
    def __str__(self):
        """Devuelve una cadena con detalles de la pelota de número: ID, participante, color y número."""
        return (
            f"[Pelota Número] ID: {self.id}, Participante: {self.participante}, "
            f"Color: {self.color}, Número: {self.numero}"
        )
