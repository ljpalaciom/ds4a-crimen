from dash import dcc, html
import dash_bootstrap_components as dbc
from dao.dao_sql import crimes_distribution_
fig = crimes_distribution_()
crimes_distribution_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Crime distribution over locality", className="card-title"),
            dcc.Graph(figure=fig)            
        ]
    )
)