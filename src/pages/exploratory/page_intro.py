from dash import dcc, html
import dash_bootstrap_components as dbc
from pages.exploratory.fact import Fact

page_intro_layout = html.Div([
    html.H1("Análisis Exploratorio", className="text-center mb-5 mt-3"),
    dbc.Row([
        dbc.Col([
                html.H2("Delitos en Bogotá, 2012-2022 Algunas cifras:", className="facts-title"),
        ], lg={"size": 5}),
        dbc.Col([
            Fact(number="01", description="* En el año 2021 los crímenes en las localidades de Kennedy y Suba (las de las cifras más altas en el histórico) se duplicaron con respecto a las cifras del 2016"),
            Fact(number="02", color="yellow", description="* Cerca de una tercera parte de los delitos que se denuncian en la ciudad corresponde al Hurto a personas"),
            Fact(number="03", color="green", description="""
            * En algunos delitos las principales víctimas son de un sexo específico: 
            Violencia intrafamiliar:  75% son mujeres.
            Homicidios: 90% son hombres."""),
        ], lg={"size": 5}),
    ], align="center" ,justify="center"),
],  className="page-intro")