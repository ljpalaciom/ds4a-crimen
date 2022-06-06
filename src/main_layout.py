from dash import Dash, dcc, html, Input, Output, callback
from pages.exploratory import page as exploratory_page
from pages.prediction import page as prediction_page

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Nav('NavBar'),
    html.Div(id='page-content')
])