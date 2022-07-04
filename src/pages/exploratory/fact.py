from dash import dcc, html
import dash_bootstrap_components as dbc


def Fact(number, description, color="purple"):
    fact_layout = html.Div([
        dbc.Row([
            dbc.Col([
                    html.Div(number, className="number"),
            ], width=3),
            dbc.Col([
                html.P(description),
            ], width=9, className="description"),
        ], align="center",justify="center"),
    ], className=f"fact fact--{color}"
    )
    return fact_layout