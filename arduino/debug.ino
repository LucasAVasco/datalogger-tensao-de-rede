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
	vpk = int ((sin(value) + 1.0) * 511);
	value += 0.1;

	// Envia o inteiro em dois bytes
	if (Serial.write(vpk >> 8))
		Serial.write(vpk);

	// Leve atraso
	delay(10);
}
