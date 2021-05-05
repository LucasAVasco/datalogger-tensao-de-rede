# coding=UTF-8

"""Módulo com as classes de configuração."""


# Módulos
import matplotlib.pyplot as plt
import re
import myModules.readFile as readFile


class graph:
    """
    Classe de um gráfico.

    Contém as variáveis e funções relacionadas
    à um grpafico. Desde a configuração, até o
    processamento e exportação do gráfico em png.
    """

    def __init__(self, name):
        """Função de inicialização."""
        # Variáveis
        self.name = name
        self.title = ''
        self.day = 0
        self.month = 0
        self.year = 0
        self.begin_minute = 0
        self.begin_hour = 0
        self.end_minute = 0
        self.end_hour = 0

        # Booleanos que definem os dados plotados
        self.hasVpkPlot = False
        self.hasRmsPlot = False
        self.hasMedPlot = False

        # Vetores de dados
        self.timeVet = []
        self.vpkVet = []
        self.medVet = []
        self.rmsVet = []

    def readProperties(self, input_file):
        """Lee as propriedades de um arquivo de configuração."""
        while True:
            line = readFile.getNextLine(input_file)

            if line[0] == '{':  # Inicia
                continue

            if line[0] == '}':  # Finaliza
                break

            # Recebe a propriedade e formata
            propertie = re.split(':', line, 1)
            propertie[0] = re.sub(' ', '', propertie[0])
            propertie[1] = re.sub(' ', '', propertie[1])

            # Para cada propriedade:
            if propertie[0] == "title":
                self.title = propertie[1]

            elif propertie[0] == "day":
                time = re.split('/', propertie[1])

                self.year = int(time[0])
                self.month = int(time[1])
                self.day = int(time[2])

            elif propertie[0] == "init":
                time = re.split('-', propertie[1])

                self.begin_hour = int(time[0])
                self.begin_minute = int(time[1])

            elif propertie[0] == "end":
                time = re.split('-', propertie[1])

                self.end_hour = int(time[0])
                self.end_minute = int(time[1])

            elif propertie[0] == "plotVpk":
                self.hasVpkPlot = bool(propertie[1])

            elif propertie[0] == "plotRms":
                self.hasRmsPlot = bool(propertie[1])

            elif propertie[0] == "plotMed":
                self.hasMedPlot = bool(propertie[1])

    def addFile(self, year, month, day, hour, minute):
        """Adiciona os dados de um arquivo '.csv' às variáveis desse objeto."""
        # Dados de tempo
        month = readFile.format_value(month)
        day = readFile.format_value(day)
        hour = readFile.format_value(hour)
        minute = readFile.format_value(minute)

        # Abre o arquivo '.csv' com os dados
        input_file = open(
                "../get-data/data/" + str(year) + "-" + str(month) + "-" +
                str(day) + '/' + str(hour) + "-" + str(minute) + ".csv", 'r'
                )

        while True:
            line = input_file.readline()
            if line == '':
                break

            # Adiciona os valores aos respectivos vetores
            properties = re.split(',', line)
            self.timeVet.append(float(properties[0]))
            self.vpkVet.append(float(properties[2]))
            self.medVet.append(float(properties[3]))
            self.rmsVet.append(float(properties[4]))

        # Fecha o arquivo
        input_file.close()

    def addAllFiles(self):
        """Adiciona os dados de todos os arquivos configurados."""
        # Tempo (hora e minuto) do arquivo atual
        hour = self.begin_hour
        minute = self.begin_minute

        while True:
            # Lee o arquivo atual
            self.addFile(self.year, self.month, self.day, hour, minute)

            # Finaliza a leitura de arquivos
            if hour == self.end_hour and minute == self.end_minute:
                break

            # Atualiza as variáveis de tempo
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1

    def plot(self):
        """Cria o gráfico."""
        # Define o título
        plt.title(self.title)

        ylabel = ''

        # Plota os gráficos que devem ser plotados
        if self.hasVpkPlot:
            plt.plot(self.timeVet, self.vpkVet)
            ylabel += " Vpk "

        if self.hasRmsPlot:
            plt.plot(self.timeVet, self.rmsVet)
            ylabel += " Rms "

        if self.hasMedPlot:
            plt.plot(self.timeVet, self.medVet)
            ylabel += " Med "

        # Define as outras propriedades do gráfico
        plt.ylabel(ylabel + "(V)")
        plt.xlabel("time (s)")
        plt.ylim(0, 360)

        # Exporta e limpa o gráfico
        plt.savefig("interface/" + self.name + ".png")
        plt.clf()

    def write(self):
        """
        Escreve um valor armazenado nesse objeto na tela.

        Essa função é apenas para prototipação.
        """
        print(self.timeVet)
