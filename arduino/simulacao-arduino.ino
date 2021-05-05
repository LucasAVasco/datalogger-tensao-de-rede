#include <math.h>


/// Macros
#define ANALOG_PIN A0


/// Variáveis
int vpk;
float value = 0;

/// Constantes
byte secBit = 0b1 << 7;


/// Inicialização
void setup()
{
	// Inicia a comunicação serial
	Serial.begin(9600);
}


/// Loop principal
void loop()
{
	// Gera o atraso da leitura de tensão
	vpk = analogRead(ANALOG_PIN);

	// Para prototipação
	value = float (micros()) * 120 * M_PI / 1000000;
	vpk = int ((sin(value) + 1.0) * 511);

	// Envia o inteiro em dois bytes
	Serial.write((vpk >> 5) & 0b11111);
	Serial.write((vpk & 0b11111) | secBit);
}
