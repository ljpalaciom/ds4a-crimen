from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dao.dao_sql import crimes_over_time_day, min_date, max_date, crimes_amount_last_day
from datetime import date, datetime, timedelta
from prediction.prediction import PredictionModelArima
import plotly.express as px
import plotly.graph_objects as go

min_date = min_date()
max_date_data = max_date()
max_date_prediction = max_date_data + timedelta(days=40)
model = PredictionModelArima()

layout = html.Div(
    [
        html.H1("Predicción de crimenes"),
        dbc.CardBody(
            [            
                dcc.DatePickerRange(
                    id="my-date-picker-range",
                    min_date_allowed=min_date,
                    max_date_allowed=max_date_prediction,
                    initial_visible_month=max_date_prediction,
                    start_date=min_date,
                    end_date=max_date_prediction,
                ),
                dcc.Loading(
                    id="loading",
                    type="default",
                    children=[html.Div(id="loading-prediction-time-series"), dcc.Graph(id="prediction-fig")],
                ),
            ]
        ),
    ]
)


@callback(
    Output("prediction-fig", "figure"),
    Output("loading-prediction-time-series", "children"),
    Input("my-date-picker-range", "start_date"),
    Input("my-date-picker-range", "end_date"),
)
def update_output(start_date, end_date):
    if datetime.strptime(end_date, "%Y-%m-%d").date() > max_date_data:
        fig = crimes_over_time_day(start_date, date.today())
        predictions = model.predict('all', datetime(max_date_data.year, max_date_data.month, max_date_data.day), datetime.strptime(end_date, "%Y-%m-%d"))
        predictions = predictions.reset_index().rename(columns={"index":"fecha", 0: "crimes"})
        fig.add_trace(go.Scatter(x=predictions.fecha, y=predictions.crimes, mode='lines', line={'dash': 'dash'}))
    else: 
        fig = crimes_over_time_day(start_date, end_date)
    return fig, False
