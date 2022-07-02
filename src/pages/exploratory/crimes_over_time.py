from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dao.dao_sql import crimes_over_time_, min_date, max_date
from datetime import date

min_date = min_date()
max_date = max_date()

crimes_over_time_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Numero de crimenes en el tiempo", className="card-title"),
            dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=min_date,
                max_date_allowed=max_date,
                initial_visible_month=max_date,
                start_date=min_date,
                end_date=max_date
            ),
            dcc.Loading(
                id="loading",
                type="default",
                children=[html.Div(id="loading-output"), dcc.Graph(id="fig")]
            )
        ]
    )
)

@callback(
    Output('fig', 'figure'),
    Output('loading-output','children'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(start_date, end_date):
    fig = crimes_over_time_(start_date, end_date)
    return fig, False