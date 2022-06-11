import pandas as pd 
import os

def getCrimes(year):
    file_path = os.path.dirname(__file__)
    rel_path = "../../data/crimenes_"+year+".csv" 
    path = os.path.join(file_path, rel_path)
    crime =  pd.read_csv(path)
    # Drop first column of dataframe
    crime = crime.iloc[: , 1:]
    return crime

def getAllCrimes():
    crime_2018 = getCrimes("2019")
    crime_2019 = getCrimes("2020")
    crime_2020 = getCrimes("2021")
    crime_2021 = getCrimes("2022")
    crimes = pd.concat([crime_2018, crime_2019,crime_2020, crime_2021], ignore_index=True)
    # transform to correct data types
    crimes['Numero hechos'] = crimes['Numero hechos'].astype(int)
    crimes['Nro del Mes'] = crimes['Nro del Mes'].astype(int)
    crimes['year'] = crimes['year'].astype(int)
    # Create date column
    crimes['date'] = pd.to_datetime(crimes['year'].astype(str) + crimes['Nro del Mes'].astype(str), format='%Y%m')
    return crimes

def get_crimes_by_month():
    crimes = getAllCrimes()
    crimes_by_month = crimes.groupby(crimes["date"].dt.to_period("M")).size().reset_index(name='crime ammount')
    crimes_by_month['date'] = crimes_by_month['date'].apply(lambda period: period.to_timestamp()) 
    return crimes_by_month

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