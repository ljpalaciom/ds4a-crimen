from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    brand="Crime Prediction DashBoard - Team 234",
    brand_href="#",
    color="primary",
    dark=True,
)

layout = dbc.Container(html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
]), id="main-container")