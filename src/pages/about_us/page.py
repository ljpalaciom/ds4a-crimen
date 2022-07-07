from dash import dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
from pages.about_us.participant import Participant


layout = html.Div([
    dbc.Row([
        dbc.Col(Participant("https://ds4a-234.s3.amazonaws.com/foto_Anthony.jpg", 'Anthony Jason Vargas Sepulveda', 'Ingeniero Sistemas','Senior Software Engineer', 'https://www.linkedin.com/in/anthony-jason-vargas-sepulveda-a504b711a/'), lg={"size": 6}),
        dbc.Col(Participant("https://ds4a-234.s3.amazonaws.com/luis.jpg", 'Luis Javier Palacio Mesa', 'Ingeniero de sistemas','Estudiante - Maestría en Ciencias de los Datos y Analítica', 'https://www.linkedin.com/in/luis-javier-palacio-mesa/'), lg={"size": 6}),
        dbc.Col(Participant("https://ds4a-234.s3.amazonaws.com/marp.jpg", 'Margui Angélica Romero Pinedo', 'Matemática','PhD en Matemática Aplicada', 'https://www.linkedin.com/in/margui-a-romero-pinedo-722942233/'), lg={"size": 6}),
        dbc.Col(Participant("https://ds4a-234.s3.amazonaws.com/Jose+F.jpg", 'Jose Fernando Duarte Alvarado', 'Economista / Administrador','Business Inteligence Specialist', 'https://www.linkedin.com/in/jose-fernando-duarte-alvarado/'), lg={"size": 6}),
        dbc.Col(Participant("https://ds4a-234.s3.amazonaws.com/Juan.jpg", 'Juan David Ayala Nariño', 'Ingeniero Industrial', ''), lg={"size": 6}),
        dbc.Col(Participant("https://ds4a-234.s3.amazonaws.com/andres.jpg", 'Andres Felipe Esteban Bautista', 'Ingeniero electricista','Estudiante - Maestría en Automatización Industrial', 'https://www.linkedin.com/in/andres-esteban-90ba031b5/'), lg={"size": 6}),
        dbc.Col(Participant("https://ds4a-234.s3.amazonaws.com/AlbertoM.jpg", 'Alberto Enrique Mercado Manotas', 'Ingeniero Electronico','', 'https://www.linkedin.com/in/alberto-enrique-mercado-manotas-882a59232/'), lg={"size": 6}),
         dbc.Col(Participant("https://ds4a-234.s3.amazonaws.com/Foto_Miguel.jpg", 'Miguel Castaño Marín', 'Ingeniero Mecánico','', 'www.linkedin.com/in/miguel-castano'), lg={"size": 6}),
        ], align="center", justify="left"), 
], id="about-us")
