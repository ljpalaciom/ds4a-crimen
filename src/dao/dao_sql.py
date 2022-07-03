import os
from xml.dom.minidom import TypeInfo
import numpy as np
import psycopg2
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px
import unidecode
from datetime import date

def postgres_connect():
    load_dotenv()
    host_db = os.getenv('POSTGRES_ADDRESS')
    database_db = os.getenv('POSTGRES_DBNAME')
    password_db = os.getenv('POSTGRES_PASSWORD')
    user_db = os.getenv('POSTGRES_USERNAME')
    try:  
        conexion = psycopg2.connect(
        host=host_db,
        database=database_db,
        user=user_db,
        password=password_db)
        cur = conexion.cursor()
        return cur
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def statement(sql_query):
    cur = postgres_connect()
    cur.execute(sql_query)
    db_version = cur.fetchall()
    cur.close()
    return db_version

def most_frequent_crimes_():
    most_frequent_crimes = pd.DataFrame(statement("""select delito, sum(numero_hechos) as sum from crimesall
                                                    group by delito
                                                    order by sum desc
                                                    limit 10
                                                    """))
    most_frequent_crimes.columns = ['crime','crime ammount']
    most_frequent_crimes.set_index('crime')
    fig = px.pie(most_frequent_crimes, names= 'crime', values='crime ammount')
    return fig

def crimes_over_time_day(start_date, end_date):
    crimes_by_day = pd.DataFrame(statement(f"""
    SELECT fecha, SUM(numero_hechos) as sum FROM crimesall
    WHERE fecha BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY fecha
    """))
    crimes_by_day.columns = ['date','crime ammount']
    crimes_by_day.set_index('date')
    fig = px.line(crimes_by_day, x='date', y="crime ammount")
    return fig


def crimes_over_time_month(start_date, end_date):
    crimes_by_day = pd.DataFrame(statement(f"""
    SELECT DATE_TRUNC('month', fecha), SUM(numero_hechos) as sum FROM crimesall
    WHERE fecha BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY DATE_TRUNC('month', fecha)
    """))
    crimes_by_day.columns = ['date','crime ammount']
    crimes_by_day.set_index('date')
    fig = px.line(crimes_by_day, x='date', y="crime ammount")
    return fig

def crimes_distribution_():
    crimes_distribution = pd.DataFrame(statement("""
    select localidad, sum(numero_hechos) as sum from crimesall group by localidad 
    ORDER BY sum DESC
    """
    ))
    crimes_distribution.columns = ['localidad','crime ammount']
    crimes_distribution.set_index('localidad')
    fig = px.bar(crimes_distribution, x='localidad', y="crime ammount")
    return fig

def gender_distribution_():
    gender_distribution = pd.DataFrame(statement("select sexo, sum(numero_hechos) as sum from crimesall group by sexo"))
    gender_distribution.columns = ['gender','crime ammount']
    gender_distribution.set_index('gender')
    fig = px.pie(gender_distribution, names='gender', values="crime ammount",color="crime ammount", color_discrete_sequence=px.colors.qualitative.G10)
    return fig

def get_crimes_by_locality_year(year):
    crimes = pd.DataFrame(statement(f"""select * from mapa{year}"""))    
    crimes.columns = ['localidad','numero hechos']
    
    crimes.localidad = [localidades[5:] for localidades in crimes.localidad]
    crimes.fillna(0, inplace=True)
    crimes['numero hechos'] = crimes['numero hechos'].astype(int)

    for i in range(len(crimes)):        
        if crimes.localidad[i] != 'ANTONIO NARIÑO':
            crimes.loc[i,'localidad'] = unidecode.unidecode(crimes.loc[i,'localidad'])

    return crimes

def most_affected_time_of_day():
    crimes = pd.DataFrame(statement("""
    select rango_dia, sum(numero_hechos) as total from crimesall
    group by rango_dia
    order by total desc"""))
    crimes.columns = ['rango_dia','numero_hechos']
    crimes.set_index('rango_dia')
    rango_dia = crimes.rango_dia[0]
    crimes['porcentaje'] = (crimes.numero_hechos/crimes.numero_hechos.sum())*100
    porcentaje = round(crimes.porcentaje[0],2)
    return rango_dia,porcentaje


def min_date():
    min = statement("""
     SELECT MIN(fecha) FROM crimesall;
    """
    )[0][0]
    return min

def max_date():
    max = statement("""
     SELECT MAX(fecha) FROM crimesall;
    """
    )[0][0]
    return max

def highest_predicted_crimes(localidad):
    crimes = pd.DataFrame(statement(f"""select localidad , delito ,sum(numero_hechos) as total from crimesall
where localidad = '{localidad}'
group by localidad, delito
order by total desc"""))
    crimes.columns = ['localidad','delito','numero_hechos']
    crimes['porcentaje'] = (crimes.numero_hechos/crimes.numero_hechos.sum())*100
    porcentaje = round(crimes.porcentaje[0],2)
    localidades = crimes.localidad[0][5:]
    delito = crimes.delito[0]
    return localidades,delito,porcentaje

def top_trending():
    mes = date.today().month
    top_trending = pd.DataFrame(statement(f"""
    select localidad, delito, nro_mes ,sum(numero_hechos) as total from crimesall
    where nro_mes = '{mes}'
    group by localidad, delito, nro_mes
    order by total desc
    limit 3"""))
    top_trending.columns = ['localidad','delito','nro mes','crime ammount']
    top_trending.localidad = [localidades[5:] for localidades in top_trending.localidad]    
    data1 = f"{top_trending.delito[0]} en {top_trending.localidad[0]}"
    data2 = f"{top_trending.delito[1]} en {top_trending.localidad[1]}"
    data3 = f"{top_trending.delito[2]} en {top_trending.localidad[2]}"
    return data1,data2,data3


def mes ():
    mes = date.today().month
    mesesDic = {
    "1":'Enero',
    "2":'Febrero',
    "3":'Marzo',
    "4":'Abril',
    "5":'Mayo',
    "6":'Junio',
    "7":'Julio',
    "8":'Agosto',
    "9":'Septiembre',
    "10":'Octubre',
    "11":'Noviembre',
    "12":'Diciembre'
}
    return mesesDic[str(mes)]


def localidades():
    localidades = pd.DataFrame(statement(f"""
    SELECT distinct(localidad)
    FROM crimesall
    """))
    return localidades[0].values


def weapon_use(localidad=None):
    weapon_use = pd.DataFrame(statement(f"""
    SELECT arma, sexo, SUM(numero_hechos) as total FROM crimesall
    {f"WHERE localidad = '{localidad}'" if localidad else ' '}
    GROUP BY arma, sexo
    ORDER BY total DESC
    LIMIT 10;
    """))
    weapon_use.columns = ["arma", "Sexo Victima", 'total']
    weapon_use.set_index('arma')
    fig = px.bar(
        weapon_use,
        x="arma",
        y="total",
        color="Sexo Victima"
    )
    return fig


def top_weapons():
    top_weapons = pd.DataFrame(statement(f"""
    SELECT arma, SUM(numero_hechos) AS total FROM crimesall
    GROUP BY arma
    ORDER by total DESC
    LIMIT 10;
    """))
    top_weapons.columns = ["arma", 'total']
    top_weapons_list = top_weapons['arma'].values
    return top_weapons_list

def crime_by_weapon(weapon):
    crime_by_weapon = pd.DataFrame(statement(f"""
    SELECT delito, SUM(numero_hechos) AS total FROM crimesall
    WHERE arma = '{weapon}'
    GROUP BY arma, delito
    ORDER by total DESC
    LIMIT 10;
    """))
    crime_by_weapon.columns = ["delito", 'total']
    return crime_by_weapon