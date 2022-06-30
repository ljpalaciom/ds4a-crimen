from dash import dcc, html
import dash_bootstrap_components as dbc

predictive_model_layout = dbc.Card(
    className="prediction-link",
    children = dbc.CardBody(
        [
            dbc.CardLink(["Predicción de Crimenes", html.I(className="bi bi-arrow-right-square")], href="/prediction"),
        ]
    )
)