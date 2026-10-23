"""Módulo de validaciones: todas las entradas del usuario pasan por aquí."""

def leer_texto(mensaje):
    """Pide un texto y rechaza cadenas vacías."""
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("Error: El campo no puede estar vacío")


def leer_entero_positivo(mensaje):
    """Pide un entero > 0. Reintenta ante ValueError."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: El valor tiene que ser mayor que 0")
        except ValueError:
            print("Error: Ingrese un número entero válido")


def leer_decimal_positivo(mensaje):
    """Pide un decimal > 0 (se usa para productos por litro)."""
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
            if valor > 0:
                return valor
            print("Error: El valor tiene que ser mayor que 0")
        except ValueError:
            print("Error: Ingrese un número válido")


def leer_opcion(mensaje, minimo, maximo):
    """Pide una opción de menú dentro de un rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: Opción fuera de rango ({minimo}-{maximo})")
        except ValueError:
            print("Error: Ingrese un número entero válido")
