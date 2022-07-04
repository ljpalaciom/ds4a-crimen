from dash import dcc, html,Input, Output, callback
import dash_bootstrap_components as dbc
from dao.dao_sql import most_affected_time_of_day, highest_predicted_crimes,top_trending,mes, localidades

localidades_result = localidades()
time_of_day, porcentaje = most_affected_time_of_day()
top1,top2,top3 = top_trending()


highest_crimes = dbc.Card(
    dbc.CardBody(
        [   
            html.H1("Delito mas reportado por localidad", className="card-title"),
            html.P('Seleccione la localidad que desea consultar:'),
            
            dcc.Dropdown(id="slct_localidad",
                 options=localidades_result,
                 multi=False,
                 clearable=False,
                 value=localidades_result[0],
                 style={'width': "60%", 'margin-left': 'auto', 'margin-right': 'auto', 'margin-top': '10px', 'margin-bottom': '10px'},
                 ),
            html.H6( children=[] ,id='output_container2', className="card-text"),
            
            
                
            
        ]
    )
)
@callback(
            Output(component_id='output_container2', component_property='children'),
            Input(component_id='slct_localidad', component_property='value')
        )
def update_output(value):
    delito,porcentaje = highest_predicted_crimes(value)
    return f"""Localidad: {value} \n
    {delito} - ({porcentaje}%) """
    
affected_time_day = dbc.Card(
    dbc.CardBody(
        [
            html.H1("Hora del dia mas afectada", className="card-title"),
            html.P(
                f"{time_of_day} ({porcentaje}%)",
                className="card-text",
            ),
        ]
    )
)

trending_felonies = dbc.Card(
    dbc.CardBody(
        [
            html.H1(f"Ranking delitos en {mes()}", className="card-title"),
            html.P(
                top1,
                className="card-text",
            ),
              html.P(
                top2,
                className="card-text",
            ),
              html.P(
                top3,
                className="card-text",
            ),
        ]
    )
)