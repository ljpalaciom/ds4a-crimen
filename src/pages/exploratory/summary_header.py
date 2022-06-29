from dash import dcc, html
import dash_bootstrap_components as dbc
from dao.dao_sql import most_affected_time_of_day
time_of_day, porcentaje = most_affected_time_of_day()
highest_crimes = dbc.Card(
    dbc.CardBody(
        [
            html.H1("Highest Predicted Crime", className="card-title"),
            html.H6("Locality Chapinero", className="card-subtitle"),
            html.P(
                "Thievery (33%)",
                className="card-text",
            ),
        ]
    )
)

affected_time_day = dbc.Card(
    dbc.CardBody(
        [
            html.H1("Most Affected Time of day", className="card-title"),
            html.P(
                f"{time_of_day} ({porcentaje}%)",
                className="card-text",
            ),
        ]
    )
)

trending_felonies = dbc.Card(
    dbc.CardBody(
        [
            html.H1("Top Trending felonies", className="card-title"),
            html.P(
                "Robo de ganado en Usme",
                className="card-text",
            ),
              html.P(
                "Homicidios en la Candelaria",
                className="card-text",
            ),
              html.P(
                "Hurto a personas en Usaquén",
                className="card-text",
            ),
        ]
    )
)