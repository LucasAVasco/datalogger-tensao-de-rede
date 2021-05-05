# coding=UTF-8


"""
Gera a interface gráfica na no navegador.

Utiliza as bibliotecas Dash e Plotly
"""


# Bibliotecas
import plotly.graph_objects as go
import myModules.configClass
import dash
import dash_html_components as html
import dash_core_components as dcc
import webbrowser


# Variváveis
figures = []


# Funções
def add_graph(graph):
    """Adiciona um gráfico a interface de navegador."""
    global figures

    figures.append(go.Figure(
        {
            "layout": {
                "title": {
                    "text": graph.title
                    }
                }
            }
        ))

    if graph.hasRmsPlot:
        figures[-1].add_trace(go.Scatter(x=graph.timeVet, y=graph.rmsVet))

    if graph.hasMedPlot:
        figures[-1].add_trace(go.Scatter(x=graph.timeVet, y=graph.medVet))

    if graph.hasVpkPlot:
        figures[-1].add_trace(go.Scatter(x=graph.timeVet, y=graph.vpkVet))


def add_all_graphs(graphs):
    """Adiciona todos os gráficos a interface de navegador."""
    for loop in graphs:
        add_graph(loop)


def show():
    """Mostra a interface de navegador."""
    global figures
    global titles

    app = dash.Dash(__name__)

    site = [html.H1(
        style={
            "text-align": "center",
            },
        children="Datalogger Tensão de Rede")
        ]

    num = 0
    for loop in figures:
        site.append(dcc.Graph(id="Fig" + str(num), figure=loop))
        num += 1

    app.layout = html.Div(style={
        "font-family": "Arial"
        }, children=site)

    webbrowser.open_new_tab('http://127.0.0.1:8050')
    app.run_server()
