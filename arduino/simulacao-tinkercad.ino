/// Macros
#define ANALOG_PIN A0


/// Variáveis
int vpk;
long value;


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

	// Dentro do DEBUG do Tinkercad
	value = (long(vpk) - 511)*250/512;
	Serial.print(value);
	Serial.print('\n');

	delay(10);
}
