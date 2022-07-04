from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
from dao.dao_sql import crimes_vs_population

crimes_vs_population_layout = dbc.Card(
    dbc.CardBody(
        [
            dcc.Slider(2015, 2022, 1,
            marks={
                2015: '2015',
                2016: '2016',
                2017: '2017',
                2018: '2018',
                2019: '2019',
                2020: '2020',
                2021: '2021',
                2022: '2022',
            },
               value=2015,
               id='year-slider'
            ),
            dcc.Loading(
                id="loading",
                type="default",
                children=[html.Div(id="loading-c_p"), dcc.Graph(id="c_p_fig")]
            )
        ]
    )
)

@callback(
    Output('c_p_fig', 'figure'),
    Output('loading-c_p','children'),
    Input('year-slider', 'value'))
def update_output(year):
    fig = crimes_vs_population(year)
    return fig,False