from dash import dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
from pages.exploratory.summary_header import highest_crimes, affected_time_day, trending_felonies
from dao.dao_csv import getAllCrimes

crimes = getAllCrimes()

layout = html.Div([
   # dash_table.DataTable(crimes.head().to_dict('records'), [{"name": i, "id": i} for i in crimes.columns]),
   dbc.CardGroup(
            [
                highest_crimes,
                affected_time_day,
                trending_felonies,
            ]
        ),
    html.Div(id='page-1-display-value'),
    dcc.Link('Go to prediction', href='/prediction')
], id="exploratory")
