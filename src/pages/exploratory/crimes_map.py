import numpy as np
import pandas as pd
import plotly.express as px
import urllib.request, json
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback
from dao.dao_sql import get_crimes_by_locality_year

# ------------------------------------------------------------------------------
with open('data/geojson/loca.geojson') as f:
    localidades = json.load(f)
# App layout
map_layout = html.Div([
    html.P('Seleccione el año que desea consultar:'),
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2010", "value": 2010},
                     {"label": "2011", "value": 2011},
                     {"label": "2012", "value": 2012},
                     {"label": "2013", "value": 2013},
                     {"label": "2014", "value": 2014},
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020},
                     {"label": "2021", "value": 2021},
                     {"label": "2022", "value": 2022}],
                 multi=False,
                 value=2010,
                 style={'width': "40%"}
                 ),
    html.Div(id='output_container', children=[]),
    html.Br(),
     dcc.Loading(
            id="loading-1",
            type="default",
            children=[html.Div(id="loading-output-1"), dcc.Graph(id='my_bee_map')]
        ),
])

@callback(
    Output(component_id='output_container', component_property='children'),
    Output(component_id='my_bee_map', component_property='figure'),
    Output(component_id='loading-output-1', component_property='children'),
    Input(component_id='slct_year', component_property='value')
)
def update_graph(option_slctd):
    container = "Número Crimenes por localidad para el año: {}".format(option_slctd)
    fig = None
    crimes_locality = get_crimes_by_locality_year(option_slctd)
    # Plotly Express
    fig = px.choropleth(crimes_locality,
        geojson=localidades,
        color="numero hechos",
        locations="localidad",
        featureidkey="properties.LocNombre",
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'numero hechos': 'Total crimes'}
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, dragmode=False)
    
    return container, fig, True