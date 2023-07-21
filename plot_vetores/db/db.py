import pandas as pd

BASE_VETOR_URL = "mysql+pymysql://prometheus:12345@0.0.0.0:3306/data_vector"

def cria_coordenadas():
    coordenadas = pd.read_sql_table('coordenadas', BASE_VETOR_URL)  
    return coordenadas

def cria_magnitudes():
    magnitudes = pd.read_sql_table('magnitude', BASE_VETOR_URL)   
    return magnitudes