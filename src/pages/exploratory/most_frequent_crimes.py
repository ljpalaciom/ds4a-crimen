from dash import dcc, html
import dash_bootstrap_components as dbc
from dao.dao_sql import most_frequent_crimes_
fig = most_frequent_crimes_()
most_frequent_crimes_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Crimenes mas frecuentes", className="card-title"),
            dcc.Graph(figure=fig)
        ]
    )
)