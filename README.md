# Datalogger de Tensão da rede



Utiliza Arduino Leonardo para ler a etrada de tensão da rede e enviar para um computador. O computador, executando um script python, lê os dados enviados e processa eles. Um outro script, quando executado, salva os dados processados e gera gráficos dele.



## Módulos Externos necessários:
* Matplotlib
* Pyserial
* Plotly
* Dash
* Pandas



Para instalar os módulos, pode-se utilizar o PIP3:

```
$ pip3 install matplotlib pyserial plotly dash pandas
```


## A fazer:
- [x] Verificar se os dados existem antes de gerar os gráficos
- [x] Arrumar o posicionamento do título do gráfico na interface
- [x] Finalizar a interface
