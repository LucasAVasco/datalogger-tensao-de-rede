#include <math.h>


/// Macros
#define ANALOG_PIN A0


/// Variáveis
int vpk;
float value = 0;


/// Inicialização
void setup()
{
	// Inicia a comunicação serial
	Serial.begin(9600);

	// Espera até o código python estiver carregado
	while (Serial.available() == 0)
	{
		delay(100);
	}
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
	if (Serial.write(vpk >> 8))
		Serial.write(vpk);
}
