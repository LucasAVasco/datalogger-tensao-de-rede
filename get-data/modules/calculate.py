
"""
Funções de análise.

Este módulo possui as funções de análise
usadas para analisar as amostras obtidas.
"""


# Importa os módulos necessários
import math


def media(list_var):
    """Retorna a média de uma lista de valores."""
    return sum(list_var)/len(list_var)


def rms(list_var):
    """Retorna o valor eficaz de uma lista de valores."""
    value = 0

    for loop in list_var:
        value += loop**2

    value = math.sqrt(value/len(list_var))

    return value


def vpk(list_var):
    """Retorna o maior valor, em módulo, de uma lista de valores."""
    max_value = max(list_var)
    min_value = min(list_var)

    if max_value > abs(min_value):
        return max_value

    else:
        return abs(min_value)
