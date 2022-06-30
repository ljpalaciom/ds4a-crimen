from dash import dcc, html,Input, Output, callback
import dash_bootstrap_components as dbc
from dao.dao_sql import most_affected_time_of_day, highest_predicted_crimes,top_trending,mes
time_of_day, porcentaje = most_affected_time_of_day()
top1,top2,top3 = top_trending()
highest_crimes = dbc.Card(
    dbc.CardBody(
        [   
            html.H1("Delito mas reportado por localidad", className="card-title"),
            html.P('Seleccione la localidad que desea consultar:'),
            
            dcc.Dropdown(id="slct_localidad",
                 options=[
                        {"label": "USAQUÉN", "value": "01 - USAQUÉN"},
                        {"label": "CHAPINERO", "value": "02 - CHAPINERO"},
                        {"label": "SANTA FE", "value": "03 - SANTA FE"},
                        {"label": "SAN CRISTÓBAL", "value": "04 - SAN CRISTÓBAL"},
                        {"label": "USME", "value": "05 - USME"},
                        {"label": "TUNJUELITO", "value": "06 - TUNJUELITO"},
                        {"label": "BOSA", "value": "07 - BOSA"},
                        {"label": "KENNEDY", "value": "08 - KENNEDY"},
                        {"label": "FONTIBÓN", "value": "09 - FONTIBÓN"},
                        {"label": "ENGATIVÁ", "value": "10 - ENGATIVÁ"},
                        {"label": "SUBA", "value": "11 - SUBA"},
                        {"label": "BARRIOS UNIDOS", "value": "12 - BARRIOS UNIDOS"},
                        {"label": "TEUSAQUILLO", "value": "13 - TEUSAQUILLO"},
                        {"label": "LOS MÁRTIRES", "value": "14 - LOS MÁRTIRES"},
                        {"label": "ANTONIO NARIÑO", "value": "15 - ANTONIO NARIÑO"},
                        {"label": "PUENTE ARANDA", "value": "16 - PUENTE ARANDA"},
                        {"label": "CANDELARIA", "value": "17 - CANDELARIA"},
                        {"label": "RAFAEL URIBE URIBE", "value": "18 - RAFAEL URIBE URIBE"},
                        {"label": "CIUDAD BOLÍVAR", "value": "19 - CIUDAD BOLÍVAR"},
                        {"label": "SUMAPAZ", "value": "20 - SUMAPAZ"}],
                 multi=False,
                 value="01 - USAQUÉN",
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
    localidad,delito,porcentaje = highest_predicted_crimes(value)
    return f"""Localidad: {localidad} \n
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