from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd 
from dao.dao_csv import getAllCrimes

import plotly.express as px

crimes = getAllCrimes()
crimes_by_month = crimes.groupby(crimes["date"].dt.to_period("M")).size().reset_index(name='crime ammount')
crimes_by_month['date'] = crimes_by_month['date'].apply(lambda period: period.to_timestamp()) 

fig = px.line(crimes_by_month, x='date', y="crime ammount")

crimes_over_time_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Crime ammount over time ", className="card-title"),
            dcc.Graph(figure=fig)
        ]
    )
)