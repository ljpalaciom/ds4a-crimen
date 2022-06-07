from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from pages.exploratory import page as exploratory_page
from pages.prediction import page as prediction_page
import main_layout

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

server = app.server

app.layout = main_layout.layout

@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/prediction':
        return prediction_page.layout
    else:
        return exploratory_page.layout

if __name__ == '__main__':
    app.run_server(debug=True)