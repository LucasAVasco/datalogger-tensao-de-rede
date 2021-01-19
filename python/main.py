#!/usr/bin/python3.8

# Bibliotecas
import serial
import serial.tools.list_ports
import time



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
output_file = open("data.csv", 'w')

# Recebe o tempo de inicio
initial_time = time.time()



# Avisa o arduino que pode começar a medir
ser.write('a')

# Lee a entrada serial, converte os valores para tensão e escreve no arquivo "data.csv"
while True:
	vpk = ser.read(2)

	vpk = (vpk[0] << 8 + vpk[1] - 511)*250/512

	output_file.write(str(time.time() - initial_time) + ',' + str(vpk) + '\n')




# Finaliza o comunicação serial com a porta do arduino
ser.close()

# Fecha o arquivo "data.csv"
output_file.close()
