# coding=UTF-8


"""
Módulo de leitura de arquivos.

Lee arquivos e formata os valores.
"""


# Módulos
import re


def getNextLine(input_file):
    """Retorna a proxima linha já formatada."""
    line = input_file.readline()

    # Espera até receber uma linha diferente de '\n'
    while line == '\n':
        line = input_file.readline()

    # Fomatatando a linha
    line = re.sub("\r", '', line)     # Compatibilidade com windows
    line = re.sub("\n$", '', line)     # New Line
    line = re.sub("^\t*", '', line)   # Tabulação
    line = re.sub("#.*$", '', line)   # Comentários de python
    line = re.sub("//.*$", '', line)  # Comentários de c++
    line = re.sub("^ *", '', line)    # Espaços no início
    line = re.sub(" *$", '', line)    # Espaços no final

    return line


def format_value(value):
    """Converte um valor para uma string de 2 caracteres."""
    value = str(value)

    if len(value) < 2:
        return '0' + value

    else:
        return value
