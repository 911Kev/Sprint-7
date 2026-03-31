"""Script para imprimir números primos del 0 al 99."""

import math


def is_prime(n):
    """Verifica si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    """Contiene la lógica principal del programa."""
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()



    