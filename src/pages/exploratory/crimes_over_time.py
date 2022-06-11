from dash import dcc, html
import dash_bootstrap_components as dbc

crimes_over_time_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Crime ammount over time ", className="card-title"),
            html.P('graph...')
        ]
    )
)