import os 
import psycopg2
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px


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
    most_frequent_crimes = pd.DataFrame(statement("""select delito, count(*) as sum from crimes
                                                    group by delito
                                                    order by sum desc
                                                    limit 10
                                                    """))
    most_frequent_crimes.columns = ['crime','crime ammount']
    most_frequent_crimes.set_index('crime')
    fig = px.pie(most_frequent_crimes, names= 'crime', values='crime ammount')
    return fig

def crimes_over_time_():
    crimes_by_month = pd.DataFrame(statement("select date, count(*) as sum from crimes group by date"))
    crimes_by_month.columns = ['date','crime ammount']
    crimes_by_month.set_index('date')
    fig = px.line(crimes_by_month, x='date', y="crime ammount")
    return fig

def crimes_distribution_():
    crimes_distribution = pd.DataFrame(statement("select localidad, count(*) as sum from crimes group by localidad"))
    crimes_distribution.columns = ['localidad','crime ammount']
    crimes_distribution.set_index('localidad')
    fig = px.bar(crimes_distribution, x='localidad', y="crime ammount")
    return fig

def gender_distribution_():
    gender_distribution = pd.DataFrame(statement("select sexo, count(*) as sum from crimes group by sexo"))
    gender_distribution.columns = ['gender','crime ammount']
    gender_distribution.set_index('gender')
    fig = px.pie(gender_distribution, names='gender', values="crime ammount",color="crime ammount", color_discrete_sequence=px.colors.qualitative.G10)
    return fig