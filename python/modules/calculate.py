# Bibliotecas
import math



##### Funções


# Retorna a média de uma lista
def media(list_var):
	return sum(list_var)/len(list_var)


# Retorna o valor eficaz de uma lista
def rms(list_var):
	value = 0

	for loop in list_var:
		value += loop**2

	value = math.sqrt(value/len(list_var))

	return value


# Retorna o maior valor (em módulo) de uma lista
def vpk(list_var):
	max_value = max(list_var)
	min_value = min(list_var)

	if max_value > abs(min_value):
		return max_value

	else:
		return abs(min_value)
