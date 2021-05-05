#!/usr/bin/python3.8
# coding=UTF-8


"""
Código principal.

Lee o arquivo de configuração 'config.txt' e os dados do diretório 'data/'
e gera os gráficos no diretório 'interface/'.
"""


# Modules
import modules.readFile as readFile
import modules.configClass as configClass
import modules.interface as interface


# Open config file
input_file = open('config.txt')


graphs = []

# Main loop
while True:
    line = readFile.getNextLine(input_file)
    if line == '':
        break

    # Configura o gráfico
    graphs.append(configClass.graph(line))
    graphs[-1].readProperties(input_file)
    graphs[-1].addAllFiles()


# Ceia a interface no navegador
interface.add_all_graphs(graphs)
interface.show()


# Close config file
input_file.close()
