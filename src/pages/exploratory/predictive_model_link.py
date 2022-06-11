from dash import dcc, html
import dash_bootstrap_components as dbc

predictive_model_layout = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardLink("Predictive Model by Locality ->", href="/prediction"),
        ]
    )
)