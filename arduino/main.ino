/// Macros
#define ANALOG_PIN A0


/// Variáveis
int vpk;

/// Constantes
const byte secBit = 0b1 << 7;


/// Inicialização
void setup()
{
	// Inicia a comunicação serial
	Serial.begin(9600);
}


/// Loop principal
void loop()
{
	// Lee o valor da tensão (0 à 1023)
	vpk = analogRead(ANALOG_PIN);

	// Envia o inteiro em dois bytes
	Serial.write((vpk >> 5) & 0b11111);
	Serial.write((vpk & 0b11111) | secBit);
}
