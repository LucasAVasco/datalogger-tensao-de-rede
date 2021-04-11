
"""
Funções de armazenamento dos dados analizados.

Contem as funções utilizadas para organizar e salvar
os dados analizados no diretório 'data/'
"""


# Importa os módulos necessários
import datetime
import os


# Variáveis locais ao módulo
last_datetime = 0
data_file = 0
last_minute = 0


def format_value(value):
    """Faz o valor possuir dois caracteres."""
    if len(value) < 2:
        return '0' + value

    else:
        return value


def get_time(date_time):
    """Retorna o tempo '%H-%M' formatado."""
    hour = str(date_time.hour)
    minute = str(date_time.minute)

    # Formata
    hour = format_value(hour)
    minute = format_value(minute)

    return hour + '-' + minute


def get_date(date_time):
    """Retorna a data '%Y-%M-%D' formatada."""
    year = str(date_time.year)
    month = str(date_time.month)
    day = str(date_time.day)

    # Formata
    year = format_value(year)
    month = format_value(month)
    day = format_value(day)

    return year + '-' + month + '-' + day


def init():
    """Inicia o armazenamemto de dados."""
    global last_datetime
    global data_file
    global last_minute

    # Atualiza as variáveis 'last_datetime' e 'last_minute'
    last_datetime = datetime.datetime.today()
    last_minute = last_datetime.minute

    # Define o diretório do arquivo
    data_file_path = 'data/' + get_date(last_datetime)

    # Gera o diretório
    try:
        os.makedirs(data_file_path)

    except FileExistsError:
        pass

    # Arbre o arquivo de dados
    data_file = open(
            data_file_path + '/' + get_time(last_datetime) + '.csv', 'w'
            )


def update():
    """Atualiza o arquivo de dados, se necessário."""
    global last_datetime
    global last_minute
    global data_file

    new_datetime = datetime.datetime.today()

    # Se o minuto mudar, muda o arquivo de dados
    if last_minute != new_datetime.minute:
        data_file.close()
        init()


def write(init_time, end_time, vpk, media, rms):
    """Escreve algo no arquivo de dados."""
    global data_file

    # atualiza o arquivo de dados
    update()

    # Salva os dados no arquivo
    data_file.write(
            str(init_time) + ',' + str(end_time) + ',' +
            str(vpk) + ',' + str(media) + ',' + str(rms) + '\n'
            )
