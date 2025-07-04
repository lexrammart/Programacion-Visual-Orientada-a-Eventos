"""
Script principal para ejecutar el sorteo de premios.

Este script lee una lista de participantes desde un archivo, genera valores aleatorios para cada participante,
y asigna premios basados en los valores de las pelotas (letra y número). Los resultados se imprimen en consola
y se guardan en un archivo de texto.
"""
from PelotaLetra import PelotaLetra
from PelotaNumero import PelotaNumero
import os

def decifrarPremio(pelota_numero, pelota_letra):
    """
    Decodifica y presenta el premio asignado a un participante basado en los atributos
    de las pelotas de número y letra. Muestra los resultados en consola y los guarda en un archivo.

    Args:
        pelota_numero (PelotaNumero): Objeto que contiene información numérica del participante.
        pelota_letra (PelotaLetra): Objeto que contiene información de letra del participante.
    """
    # Obtener atributos directamente
    color_num = pelota_numero.color
    numero = pelota_numero.numero
    color_let = pelota_letra.color
    letra = pelota_letra.letra
    participante = pelota_numero.participante  # o pelota_letra.participante

    # Mapas
    unidad_map = {
        "azul": "Xochimilco",
        "verde": "Iztapalapa",
        "rojo": "Azcapotzalco"
    }

    categoria_map = {
        "A": "Libros físicos",
        "B": "Libros electrónicos",
        "C": "Papelería",
        "D": "Souvenirs"
    }

    valor_map = {
        "amarillo": "$1000",
        "morado": "$2000",
        "rosa": "$3000"
    }

    vigencia_map = {
        1: "1 mes",
        2: "2 meses",
        3: "3 meses",
        4: "4 meses"
    }

    unidad = unidad_map.get(color_let, "Unidad desconocida")
    categoria = categoria_map.get(letra, "Categoría desconocida")
    valor = valor_map.get(color_num, "Valor desconocido")
    vigencia = vigencia_map.get(numero, "Vigencia desconocida")

    # Mostrar en consola usando __str__
    print(pelota_numero)
    print(pelota_letra)
    print(f" Premio → {categoria} en {unidad}, valor: {valor}, vigencia: {vigencia}")
    print("-" * 40)

    # Guardar en archivo
    resultado = (
        f"Participante: {participante}\n"
        f"Premio: {categoria}\n"
        f"Unidad: {unidad}\n"
        f"Valor: {valor}\n"
        f"Vigencia: {vigencia}\n"
        f"{'-'*40}\n"
    )

    with open("premios.txt", "a+", encoding="utf-8") as f:
        f.write(resultado)

def main():
    """
    Función principal que orquesta el sorteo.

    Lee los participantes desde un archivo de texto, genera valores aleatorios para cada uno,
    crea los objetos correspondientes de pelota, y determina el premio para cada participante.
    """
    try:
        with open("PVOE/Sorteo/participantes.txt", "r", encoding="utf-8") as file:
            for line in file:
                id, nombre = line.strip().split(",")

                # Crear objetos
                pelota_numero = PelotaNumero(id, nombre)
                pelota_letra = PelotaLetra(id, nombre)

                # Generar valores aleatorios
                pelota_numero.generarValor()
                pelota_numero.pintarPelota()

                pelota_letra.generarValor()
                pelota_letra.pintarPelota()

                # Ejecutar sorteo
                decifrarPremio(pelota_numero, pelota_letra)

    except FileNotFoundError as e:
        print(" Error:", e)
        print(" Directorio actual:", os.getcwd())
        print(" Archivos en este directorio:", os.listdir())
    finally:
        print(" Sorteo finalizado.")

if __name__ == "__main__":
    main()
    