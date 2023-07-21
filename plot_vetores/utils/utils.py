from pandas import DataFrame
import yaml

def cria_valores_0(coordenadas: DataFrame):
    linhas_0 = coordenadas.loc[:, 'mag'].between(0, 500, 'both')
    coordenadas.loc[linhas_0, 'mag'] = 0
    return linhas_0

def cria_valores_1000(coordenadas):
   linhas_1000 = coordenadas.loc[:, 'mag'].between(501, 1500, 'both')
   coordenadas.loc[linhas_1000, 'mag'] = 1000
   return linhas_1000

def cria_valores_2000(coordenadas):
    linhas_2000 = coordenadas.loc[:, 'mag'].between(1501, 2500, 'both')
    coordenadas.loc[linhas_2000, 'mag'] = 2000
    return linhas_2000

def cria_valores_3000(coordenadas):
    linhas_3000 = coordenadas.loc[:, 'mag'].between(2501, 3500, 'both')
    coordenadas.loc[linhas_3000, 'mag'] = 3000
    return linhas_3000

def valores_config():
    valores_config = dict()
    with open("config.yml", "r") as stream:
        try:
            valores_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)    
    return valores_config