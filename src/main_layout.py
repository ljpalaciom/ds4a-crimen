from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink([html.I(className="bi bi-graph-up nav-icon"),"Exploratory Dashboard"], href="/"), className="nav-item"),
        dbc.NavItem(dbc.NavLink([html.I(className="bi bi-graph-up-arrow nav-icon"), "Forecast Dashboard"], href="/prediction"), className="nav-item"),
    ],
    brand="Crime Prediction DashBoard - Team 234",
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