from dash import dcc, html
import dash_bootstrap_components as dbc

crimes_distribution_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Crime distribution over locality", className="card-title"),
            html.P('graph...')
        ]
    )
)