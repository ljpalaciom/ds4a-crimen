from dash import dcc, html
import dash_bootstrap_components as dbc

gender_distribution_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Victims gender distribution by crime", className="card-title"),
            html.P('graph...')
        ]
    )
)