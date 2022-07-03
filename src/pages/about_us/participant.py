from dash import dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
from pages.exploratory.summary_header import highest_crimes, affected_time_day, trending_felonies
from pages.exploratory.crimes_map import map_layout
from pages.exploratory.report_crime import report_crime_layout
from pages.exploratory.predictive_model_link import predictive_model_layout
from pages.exploratory.crimes_over_time import crimes_over_time_layout
from pages.exploratory.most_frequent_crimes import most_frequent_crimes_layout
from pages.exploratory.crimes_distribution import crimes_distribution_layout
from pages.exploratory.gender_distribution import gender_distribution_layout
from pages.exploratory.weapon_analisys import weapon_layout


def Participant(picture, name, profession, role, linkedin):
    participant_layout = html.Div([
        dbc.Row([
            dbc.Col("Picture",lg={"size": 4}),
            dbc.Col([
                html.Strong("Name"),
                html.P("Profession"),
                html.P("Role"),
                html.A("Linkedin", target="_blank")
                ],lg={"size": 8}),
            ], align="center"), 
    ], className="participant")
    return participant_layout


