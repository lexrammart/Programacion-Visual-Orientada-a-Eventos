"""
Módulo que define la clase PelotaLetra, subclase de Pelota para representar
pelotas con valor de letra en el sorteo.

Contiene la lógica para generar una letra aleatoria y pintar la pelota con un color.
"""

from Pelota import Pelota
import random as rd


class PelotaLetra(Pelota):
    """
    Subclase de Pelota que representa una pelota cuyo valor es una letra.

    Atributos:
        __letra (str): Letra asignada a la pelota. Inicialmente 'X'.

    Métodos:
        generarValor(): Asigna aleatoriamente una letra entre 'A' y 'D'.
        pintarPelota(): Cambia el color de la pelota aleatoriamente.
    """

    def __init__(self, id, participante):
        super().__init__(id, participante)
        self.__letra = "X"  # letra inicial

    @property
    def letra(self):
        return self.__letra

    @letra.setter
    def letra(self, valor):
        self.__letra = valor

    # métodos requeridos
    def generarValor(self):
        """Genera y asigna aleatoriamente una letra de la lista ['A', 'B', 'C', 'D']."""
        self.__letra = rd.choice(["A", "B", "C", "D"])

    def pintarPelota(self):
        """Selecciona aleatoriamente un color para la pelota entre 'azul', 'verde' o 'rojo'."""
        self.color = rd.choice(["azul", "verde", "rojo"])

    # decifrar premio
    def decifrarPremio(self):
        # return super().decifrarPremio()
        # Mapas
        unidad_map = {
            "azul": "Xochimilco",
            "verde": "Iztapalapa",
            "rojo": "Azcapotzalco",
        }

        categoria_map = {
            "A": "Libros físicos",
            "B": "Libros electrónicos",
            "C": "Papelería",
            "D": "Souvenirs",
        }
        pass

    # toString
    def __str__(self):
        """Devuelve una cadena con detalles de la pelota de letra: ID, participante, color y letra."""
        return (
            f"[Pelota Letra] ID: {self.id}, Participante: {self.participante}, "
            f"Color: {self.color}, Letra: {self.letra}"
        )
