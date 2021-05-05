// Bibliotecas
#include <math.h>


// Macros
#define ANALOG_PIN A0
#define S_RATE 500
#define S_DELAY 300


// Variáveis
int read_values[S_RATE];
char text[10];


// Inicialização
void setup()
{
	// Inicia a comunicação serial
	Serial.begin(9600);
}


// Loop principal
void loop()
{
	// Leitura das amostras
	for (int i = 0; i < S_RATE; i++)
	{
		read_values[i] = analogRead(ANALOG_PIN);
		delayMicroseconds(S_DELAY);
	}

	// Calcula o valor RMS
	double value, rms = 0;
	for (int i = 0; i < S_RATE; i++)
	{
		// O valor 1144 abaixo é um multiplicador que deve ser ajustado pelo usuário
		value = ((double) read_values[i] - 511 ) * 1144 / 511;
		rms += value * value;
	}

	rms = sqrt(rms/S_RATE);

	// Mostra o Valor RMS
	Serial.println((int) rms);
}
