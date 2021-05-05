# coding=UTF-8


"""
Módulo de leitura de arquivos.

Lee arquivos e formata os valores.
"""


# Módulos
import re


def getNextLine(input_file):
    """Retorna a proxima linha já formatada."""
    while True:
        line = input_file.readline()

        # Se chegou no final do arquivo
        if line == '':
            return ''

        # Fomatatando a linha
        line = re.sub("\r", '', line)     # Compatibilidade com windows
        line = re.sub("\n$", '', line)    # New Line
        line = re.sub("^\t*", '', line)   # Tabulação
        line = re.sub("#.*$", '', line)   # Comentários de python
        line = re.sub("//.*$", '', line)  # Comentários de c++
        line = re.sub("^ *", '', line)    # Espaços no início da linha
        line = re.sub(" *$", '', line)    # Espaços no final da linha

        # Se a linha não possui nenhum instrução
        if line == '':
            continue  # Le a próxima linha

        return line


def format_value(value):
    """Converte um valor para uma string de 2 caracteres."""
    value = str(value)

    if len(value) < 2:
        return '0' + value

    else:
        return value
