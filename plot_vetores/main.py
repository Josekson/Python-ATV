import pandas as pd
import matplotlib.pyplot as plt
import db.db as db
import utils.utils as utils

#Chamada da funcao que cria as coordenadas do plano 
#As funcoes sao chamadas do db.py
coordenadas = db.cria_coordenadas()
magnitudes = db.cria_magnitudes()

coordenadas.loc[:, 'mag'] = magnitudes.loc[:, 'mag']

linhas_0 = utils.cria_valores_0(coordenadas)
linhas_1000 = utils.cria_valores_1000(coordenadas)
linhas_2000 = utils.cria_valores_2000(coordenadas)
linhas_3000 = utils.cria_valores_3000(coordenadas)

coordenadas_id = coordenadas[coordenadas['id'] == 106016]

def mostrar_vetores(coordenadas: pd.DataFrame, comprimento0: bool, comprimento1: bool, comprimento2: bool, comprimento3: bool):
    
    mag_zero = coordenadas[coordenadas['mag'] == 0] * 0

    mag1000 = coordenadas[coordenadas['mag'] == 1000] * 1000


    mag2000 = coordenadas[coordenadas['mag'] == 2000] * 2000


    mag3000 = coordenadas[coordenadas['mag'] == 3000] * 3000


    ax = plt.axes(projection="3d")

    if comprimento0:
        ax.scatter3D(mag_zero.loc[:, 'x'], mag_zero.loc[:, 'y'], mag_zero.loc[:, 'z'], label="0")

    if comprimento1:
        ax.scatter3D(mag1000.loc[:, 'x'], mag1000.loc[:, 'y'], mag1000.loc[:, 'z'], label="1000")

    if comprimento2:
        ax.scatter3D(mag2000.loc[:, 'x'], mag2000.loc[:, 'y'], mag2000.loc[:, 'z'], label="2000")

    if comprimento3:
     ax.scatter3D(mag3000.loc[:, 'x'], mag3000.loc[:, 'y'], mag3000.loc[:, 'z'], label="3000")

    ax.legend(loc=1)

    plt.show()

config =  utils.valores_config()

mostrar_vetores(coordenadas_id, **config) 