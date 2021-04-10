/// Macros
#define ANALOG_PIN A0


/// Variáveis
int vpk;


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

	// Envia o inteiro em dois bytes
	if (Serial.write(vpk >> 8))
		Serial.write(vpk);
}
