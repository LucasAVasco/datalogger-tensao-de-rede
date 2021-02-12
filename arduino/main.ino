/// Macros
#define ANALOG_PIN A0

/// Macros de prototipação
//#define TINKERCAD_DEBUG
#define ARDUINO_DEBUG



/// Variáveis
int vpk;

#ifdef TINKERCAD_DEBUG
long value;
#endif

#ifdef ARDUINO_DEBUG
float value = 0;
#endif



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
	// Lee o valor da tensão (0 à 1023)
	vpk = analogRead(ANALOG_PIN);

	// Fora do DEBUG do Tinkercad
	#ifndef TINKERCAD_DEBUG

	// Para prototipação
	#ifdef ARDUINO_DEBUG
	vpk = int ((sin(value) + 1.0) * 511);
	value += 0.1;
	#endif

	// Envia o inteiro em dois bytes
	Serial.write(vpk >> 8);
	Serial.write(vpk);

	#endif


	// Dentro do DEBUG do Tinkercad
	#ifdef TINKERCAD_DEBUG
	value = (long(vpk) - 511)*250/512;
	Serial.print(value);
	Serial.print('\n');
	#endif

	delay(10);
}
