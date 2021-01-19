#!/usr/bin/python3.8



# Adicionando o path "modules/"
import sys
sys.path.append("modules/")

# Bibliotecas
import serial
import serial.tools.list_ports
import time

# Meus módulos
import calculate



# Recebe um objeto com as portas seriais
arduino_ports = serial.tools.list_ports.comports()

if len(arduino_ports) == 0:
	print("\nvoce esqueceu de conectar o arduino!\nFaça isso e reinicie o programa.\n")

	exit()

else:
	print("\nConectado à porta serial: \"" + arduino_ports[0].device + "\"\n")



# Inicia o comunicação serial com a porta do arduino
ser = serial.Serial(arduino_ports[0].device, 9600)

# Abre o arquivo "data.csv"
voltage_file = open("voltage.csv", 'w')
data_file = open("data.csv", 'w')

# Recebe o tempo de inicio
initial_time = time.time()



# Outras variáveis
last_val_neg = False
values = []
times = []



# Avisa o arduino que pode começar a medir
ser.write(1)

# Loop Principal
while True:
	# Faz a leitura serial
	val = ser.read(2)

	# converte os valores em tensão
	val = ((val[0] << 8) + val[1] - 511)*250/512

	# Atualiza a lista de tempo
	times.append(time.time() - initial_time)



	# Realiza os cálculos e reinicia o período
	if last_val_neg and val > 0:

		if len(values) > 40:

			for loop in range(len(values)):
				voltage_file.write(str(times[loop]) + ',' + str(values[loop]) + '\n')

			media = calculate.media(values)
			rms = calculate.rms(values)
			vpk = calculate.vpk(values)

			data_file.write(str(times[0]) + ',' + str(times[-1]) + ',' + str(vpk) + ',' + str(media) + ',' + str(rms) + '\n')

		# Reiniciando
		values = []
		times = []



	# Adiciona o valor da tensão à lista
	values.append(val)

	# Atualiza "last_val_pos"
	if val > 0:
		last_val_neg = False
	elif val < 0:
		last_val_neg = True



# Finaliza o comunicação serial com a porta do arduino
ser.close()

# Fecha o arquivo "data.csv"
voltage_file.close()
data_file.close()
