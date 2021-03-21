#!/usr/bin/python3.8
# coding=UTF-8


"""
Código principal.

Lee o arquivo de configuração 'config.txt' e os dados do diretório 'data/'
e gera os gráficos no diretório 'interface/'.
"""


# Modules
import matplotlib.pyplot as plt
import myModules.readFile as readFile
import myModules.configClass as configClass


# Open config file
input_file = open('config.txt')


# Main loop
while True:
    line = readFile.getNextLine(input_file)
    if line == '':
        break

    # Configura o gráfico
    graph = configClass.graph(line)
    graph.readProperties(input_file)
    graph.addAllFiles()

    # Cria o gráfico
    graph.plot()


# Close config file
input_file.close()
