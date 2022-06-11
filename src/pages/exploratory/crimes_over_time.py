from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd 
from dao.dao_csv import get_crimes_by_month

import plotly.express as px

crimes_by_month = get_crimes_by_month()

fig = px.line(crimes_by_month, x='date', y="crime ammount")

crimes_over_time_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Crime ammount over time ", className="card-title"),
            dcc.Graph(figure=fig)
        ]
    )
)