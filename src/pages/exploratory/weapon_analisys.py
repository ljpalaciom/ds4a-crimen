from dash import dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
from dao.dao_sql import weapon_use, localidades, crime_by_weapon, top_weapons
import plotly.express as px
from datetime import date

localidades = localidades()

fig = weapon_use()
top_weapons_result = top_weapons()

# fig_kennedy = weapon_use(localidad="08 - KENNEDY")
# fig_suba = weapon_use(localidad="11 - SUBA")
# fig_engativa = weapon_use(localidad="10 - ENGATIVÁ")
#fig_usaquen = weapon_use(localidad="10 - USAQUÉN")

weapon_layout = dbc.Card(
    dbc.CardBody(
        [
            html.H2("Uso de Armas", className="card-title"),
            dcc.Graph(id="weapon_fig", figure=fig),
            dbc.Row([
            # dbc.Col(
            #    [ 
            #     html.H3("Filtro por localidad", className="card-title"),
            #     dcc.Dropdown(localidades, value=localidades[0], id="weapon_localidad", placeholder="Localidades",),
            #     dcc.Graph(id="weapon_fig_filter")], 
            #     lg={"size": 6}),    
            dbc.Col(
               [ 
                html.H3("Top delitos comentidos con arma:", className="card-title"),
                dcc.Dropdown(top_weapons_result, value=top_weapons_result[0], id="weapon_filter", placeholder="Tipo de Arma",),
                ], 
                lg={"size":4}),
            dbc.Col(
               [ 
                dcc.Loading(
                id="loading",
                type="default",
                children=[
                    html.Div(id="loading-table"),
                    dash_table.DataTable(
                    id='crime_table',
                    data=[]
                )]
                )
                ], 
                lg={"size": 8}),
                
            ], align="center"),
        ]
    )
)

@callback(
    [Output("crime_table", "data"), Output('crime_table', 'columns'),  Output('loading-table','children'),],
    Input('weapon_filter', 'value')
)
def update_output(value):
   crime_by_weapon_result = crime_by_weapon(value)
   data = crime_by_weapon_result.to_dict('records')
   colums =  [{"name": i, "id": i} for i in crime_by_weapon_result.columns]
   return data, colums , False 


# @callback(
#     Output('weapon_fig_filter', 'figure'),
#     Input('weapon_localidad', 'value')
# )
# def update_output(value):
#     fig = weapon_use(value)
#     return fig
