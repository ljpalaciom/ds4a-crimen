from dash import dcc, html
import dash_bootstrap_components as dbc
from dao.dao_sql import crimes_over_time_

fig = crimes_over_time_()

crimes_over_time_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Crime ammount over time ", className="card-title"),
            dcc.Graph(figure=fig)
        ]
    )
)