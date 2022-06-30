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

layout = html.Div([
    dbc.Row([
        dbc.Col(highest_crimes, lg={"size": 4}, className="header-section"),
        dbc.Col(affected_time_day, lg={"size": 4}, className="header-section"),
        dbc.Col(trending_felonies, lg={"size": 4}, className="header-section"),
        ], align="center"),
    dbc.Row(dbc.Col(map_layout)),
    dbc.Row([
        dbc.Col(crimes_over_time_layout, lg={"size": 6}),
        dbc.Col(most_frequent_crimes_layout, lg={"size": 6}),
        ], align="center"),
    dbc.Row([
        dbc.Col(crimes_distribution_layout, lg={"size": 6}),
        dbc.Col(gender_distribution_layout, lg={"size": 6}),
        ], align="center"),
    dbc.Row([
        dbc.Col(predictive_model_layout, lg={"size": 4, "offset": 8})
        ], align="center"),    
], id="exploratory")
