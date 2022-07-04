from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dao.dao_sql import crimes_over_time_day, crimes_over_time_month, min_date, max_date
from datetime import date

min_date = min_date()
max_date = max_date()

crimes_over_time_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Serie de tiempo número de crimenes", className="card-title"),
            dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=min_date,
                max_date_allowed=max_date,
                initial_visible_month=max_date,
                start_date=min_date,
                end_date=max_date
            ),
            dbc.Row([
                dbc.Col(html.Strong('Agrupar por: '), width="auto"),
                dbc.Col(
                    dcc.RadioItems(
                    id="group-by",
                    options=['Día', 'Mes'],
                    value='Día'
                    ), width="auto", className="radio_group")
                ]),
            dcc.Loading(
                id="loading",
                type="default",
                children=[html.Div(id="loading-time-series"), dcc.Graph(id="fig")]
            )
        ]
    )
)

@callback(
    Output('fig', 'figure'),
    Output('loading-time-series','children'),
    Input('group-by', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(group_by,start_date, end_date):
    if group_by== 'Mes':
        fig = crimes_over_time_month(start_date, end_date)
    else:
        fig = crimes_over_time_day(start_date, end_date)
    return fig, False