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
	Serial.write((vpk >> 5) & 0b11111);
	Serial.write((vpk & 0b11111) | secBit);

	// Leve atraso
	delay(10);
}
