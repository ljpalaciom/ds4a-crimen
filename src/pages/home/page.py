from dash import dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
from pages.about_us.participant import Participant


layout = html.Div([
    dbc.Row([
            html.H1("Entendiendo tasas de criminalidad en Bogotá", className="text-center mb-5"),
            dbc.Col([
                html.P(["En el último año la percepción de inseguridad de los bogotanos ha sido la más alta en 6 años.  En 2021, el indicador de percepción de inseguridad en la ciudad se estimó en un 88%",html.Sup(1)]),
                html.P([
                    "Con cerca de 8 millones de habitantes y más de 1.7 millones de turitas que visitan la ciudad cada año",
                    html.Sup("2"),
                    html.Span(" ,la seguridad en la ciudad es un desafío que requiere ser analizado con detalle.")
                    ]
                ),
                html.P("Esta herramienta fue creada con el fin de entender las cifras de delitos en Bogotá, su prevalencia por sectores de la ciudad, tipos de delito, género, densidad  y su evolución en el tiempo."),
                html.Div(html.A("1. Portafolio", target="_blank", href="https://www.portafolio.co/tendencias/bogota-con-la-percepcion-de-inseguridad-mas-alta-en-6-anos-561756", className="reference")),
                html.Div(html.A("2. Cotelco", target="_blank", href="https://www.ccb.org.co/observatorio/Analisis-Economico/Analisis-Economico/Turismo/Bogota-es-el-principal-destino-turistico-de-Colombia", className="reference")),
            ], lg={"size": 5}),
            dbc.Col([
                html.A([html.Span("Análisis exploratorio", className="title"), html.I(className="bi bi-pie-chart-fill")] , href="/exploratory", className="page-link"),
                html.P("Encuentre aquí distintas consultas de los crímenes en Bogotá por localidades, su relación con el sexo de la víctima y su evolución en el tiempo durante los últimos 10 años."),
                html.A([html.Span("Predicciones", className="title"),  html.I(className="bi bi-graph-up-arrow")] , href="/prediction", className="page-link"),
                html.P("Aquí encontrará una estimación del número de crímenes diarios que ocurrirán en los siguientes días del año 2022.")
            ], lg={"size": 5, "offset": 1}),
        ], justify="center"), 
], id="home")
