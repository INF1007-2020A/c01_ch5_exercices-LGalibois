#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import math

def convert_to_absolute() -> float:
    return math.fabs(float(input("Entrez un nombre:")))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    combination = []

    for prefixe in prefixes:
        combination.append(f"{prefixe}{suffixes}")

    return combination


def prime_integer_summation() -> int:
    prime_integer = [2]
    evaluated_int = 3

    while len(prime_integer) < 100:
        is_prime = True

        for prime in prime_integer:
            if evaluated_int % prime == 0:
                is_prime = False
                break

        if is_prime:
            prime_integer.append(evaluated_int)
        evaluated_int += 2

    return sum(prime_integer)


def factorial(number: int) -> int:
    if number == 1:
        facto = 1
    else:
        facto = number * factorial(number - 1)

    return facto


def use_continue() -> None:
    for i in range(1, 10):
        if i == 5:
            continue
        else:
            print(i)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
