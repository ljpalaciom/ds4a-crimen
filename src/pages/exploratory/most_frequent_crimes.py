from dash import dcc, html
import dash_bootstrap_components as dbc

most_frequent_crimes_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Most frequent crimes", className="card-title"),
            html.P('graph...')
        ]
    )
)