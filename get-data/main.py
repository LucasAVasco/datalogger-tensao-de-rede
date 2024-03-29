#!/usr/bin/python3.8


"""
Etapa 2 - Recebimento dos dados e analise.

Esta etapa é responsável por receber os dados via comunicação serial,
convertêl-los em tensão e, depois, analisá-los. A análise consiste
em obter os valores máximo, médio e eficaz dos períodos e salválos
ordenadamente no diretório 'data/' criado por este programa.
"""


# Bibliotecas
import serial
import serial.tools.list_ports
import time
import matplotlib.pyplot as plt

# Meus módulos
import modules.calculate as calculate
import modules.save_data as save_data


# Variáveis de DEBUG
SHOW_GRAPH = False
SAVE_VOLTAGE = False


# Recebe um objeto com as portas seriais
arduino_ports = serial.tools.list_ports.comports()

if len(arduino_ports) == 0:
    print(
            "\nvoce esqueceu de conectar o arduino!\n"
            "Faça isso e reinicie o programa.\n"
        )

    exit()

else:
    print("\nConectado à porta serial: \"" + arduino_ports[0].device + "\"\n")


# Inicia o comunicação serial com a porta do arduino
ser = serial.Serial(arduino_ports[0].device, 9600)

# Inicia o armazenamento de dados
save_data.init()

# Abre o arquivo "voltage.csv"
if SAVE_VOLTAGE:
    voltage_file = open("voltage.csv", 'w')

# Tempo de referência para atualização do gráfico
last_plot_time = time.time()


# Configura o gráfico de teste
if SHOW_GRAPH:
    plt.ion()

    figure, ax = plt.subplots()
    line, = ax.plot([0], [0])

    plt.title("Tensão por Tempo")
    plt.xlabel("Tempo (ms)")
    plt.ylabel("Tensão (V)")
    plt.ylim(-353, 353)


# Outras variáveis
last_val_neg = False
values = []
times = []


# Loop Principal
while True:
    # Faz a leitura serial
    serialVal = ser.read(2)

    # Checa se os bytes estão na ordem certa
    if serialVal[0] & (0b1 << 7) or not(serialVal[1] & (0b1 << 7)):
        ser.read()
        continue

    # Junta os valores seriais lidos
    val = (serialVal[0] << 5) | (serialVal[1] & 0b11111)

    # converte os valores em tensão
    val = (val - 511) * 1144/511

    # Atualiza a lista de tempo
    times.append(time.time())

    # Adiciona o valor da tensão à lista
    values.append(val)

    # Realiza os cálculos e reinicia o período
    if last_val_neg and val > 0:

        if len(values) > 20:

            # Salva os valores da voltagem
            if SAVE_VOLTAGE:
                voltage_file.write(
                        '---------------------------------------------\n'
                        )

                for loop in range(len(values)):
                    voltage_file.write(
                            str(times[loop]) + ',' + str(values[loop]) + '\n'
                            )

            # Calcula os valores relacionados à onda
            media = calculate.media(values)
            rms = calculate.rms(values)
            vpk = calculate.vpk(values)

            # Escreve os valores calculados
            save_data.write(times[0], times[-1], vpk, media, rms)

            # Atualiza o gráfico a cada 3 segundos
            if SHOW_GRAPH and time.time() > last_plot_time + 3.0:
                last_plot_time = time.time()

                # Converte o tempo em milissegundos
                base_time = times[0]
                for loop in range(len(times)):
                    times[loop] = (times[loop] - base_time) * 1000

                # Atualiza os limites do eixo x
                plt.xlim(times[0], times[-1])

                # Atualiza os valores
                line.set_xdata(times)
                line.set_ydata(values)

                # Desenha o gráfico
                figure.canvas.draw()

                # Limpa a fila de eventos
                figure.canvas.flush_events()

        # Reiniciando
        values = []
        times = []

    # Atualiza "last_val_neg"
    if val > 0:
        last_val_neg = False
    elif val < 0:
        last_val_neg = True


# Finaliza o comunicação serial com a porta do arduino
ser.close()

# Fecha o arquivo "data.csv"
voltage_file.close()
