from dash import dcc, html
import dash_bootstrap_components as dbc
from dao.dao_sql import gender_distribution_
fig = gender_distribution_()
gender_distribution_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Victims gender distribution by crime", className="card-title"),
            dcc.Graph(figure=fig)
        ]
    )
)