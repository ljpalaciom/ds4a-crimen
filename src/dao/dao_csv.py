import pandas as pd 
import os
import unidecode

def getCrimes(year):
    file_path = os.path.dirname(__file__)
    rel_path = "../../data/daily/crimes_"+str(year)+".csv" 
    path = os.path.join(file_path, rel_path)
    crimes =  pd.read_csv(path, parse_dates=["fecha"])
    crimes = crimes.dropna(axis=0)
    crimes['numero hechos'] = crimes['numero hechos'].astype(int)
    crimes['no mes'] = crimes['no mes'].astype(int)
    crimes['year'] = crimes['year'].astype(int)
    return crimes

def getAllCrimes():
    crimes = pd.concat([getCrimes(year) for year in list(range(2010, 2023))]).reset_index(drop=True)
    return crimes

def get_crimes_by_month():
    crimes = getAllCrimes()
    crimes_by_month = crimes.groupby(crimes["fecha"].dt.to_period("M")).size().reset_index(name='crime ammount')
    crimes_by_month['fecha'] = crimes_by_month['fecha'].apply(lambda period: period.to_timestamp()) 
    return crimes_by_month

def get_crimes_by_locality_year(year):
    crimes = getCrimes(str(year))

    # Adjust the dataset in a way that we could use
    crimes_locality = crimes[crimes['year']== year].groupby('localidad')['numero hechos'].sum()
    crimes_locality = crimes_locality.reset_index()
    for i in range(len(crimes_locality)):
        if i != 14:
            crimes_locality['localidad'][i] = unidecode.unidecode(crimes_locality['localidad'][i][5:])
        else:
            crimes_locality['localidad'][i] = crimes_locality['localidad'][i][5:]
    return crimes_locality

def xml_to_csv():
    df = read_xml('https://github.com/ljpalaciom/ds4a-crimen/blob/master/data/crimenes_2019.xml?raw=true', 2019)
    df.to_csv('crimenes_2019.csv')

def read_xml(path, year): 
    df = pd.read_xml(path,
                     namespaces={"xsd": "http://www.w3.org/2001/XMLSchema"})
    # Drop first row does not have values
    df = df.iloc[1: , :]
    df = df.drop(['targetNamespace', 'complexType'] , axis=1)
    df.columns=['year', 'Registros', 'Nro del Mes', 'Mes', 'Dia', 'Rango dia', 'Localidad', 'Sexo', 'Delito', 'Modalidad', 'Arma empleada', 'Numero hechos']
    # return values for the given year
    df = df[df['year'] == year]
    return df