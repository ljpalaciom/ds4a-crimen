from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink([html.I(className="bi bi-graph-up nav-icon"), "Análisis exploratorio"], href="/exploratory"), className="nav-item"),
        dbc.NavItem(dbc.NavLink([html.I(className="bi bi-graph-up-arrow nav-icon"), "Predicción de crimenes"], href="/prediction"), className="nav-item"),
        dbc.NavItem(dbc.NavLink([html.I(className="ml-2"), "Quienes Somos"], href="/about-us"), className="nav-item"),

    ],
    brand="Crimenes en la ciudad de Bogotá - Team 234",
    brand_href="/",
    color="primary",
    dark=True,
)


layout = dbc.Container(html.Div([
    navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.I(className="bi bi-info-circle-fill me-2"),
]), id="main-container", fluid=True)