from dash import dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
from pages.about_us.participant import Participant


layout = html.Div([
    dbc.Row([
        dbc.Col(Participant("picture", 'Anthony', 'Sistemas','role', 'linkeding'), lg={"size": 6}),
        dbc.Col(Participant("picture", 'Anthony', 'Sistemas','role', 'linkeding'), lg={"size": 6}),
        dbc.Col(Participant("picture", 'Anthony', 'Sistemas','role', 'linkeding'), lg={"size": 6}),
        dbc.Col(Participant("picture", 'Anthony', 'Sistemas','role', 'linkeding'), lg={"size": 6}),
        dbc.Col(Participant("picture", 'Anthony', 'Sistemas','role', 'linkeding'), lg={"size": 6}),
        dbc.Col(Participant("picture", 'Anthony', 'Sistemas','role', 'linkeding'), lg={"size": 6}),
        dbc.Col(Participant("picture", 'Anthony', 'Sistemas','role', 'linkeding'), lg={"size": 6}),
        ], align="center", justify="left"), 
], id="about-us")
