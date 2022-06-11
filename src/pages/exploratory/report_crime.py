from dash import dcc, html
import dash_bootstrap_components as dbc

report_crime_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Report a Crime", className="card-title"),
            html.P(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare lorem vitae felis.",
                className="card-text",
            ),
            dbc.CardLink("Link to Ponal ->", href="#"),
        ]
    )
)