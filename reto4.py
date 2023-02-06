import pandas as pd
fuenteDatos=pd.read_csv("./exterior.csv")

filtrohead=fuenteDatos.head(20)
print(filtrohead)

filtrotail=fuenteDatos.tail(35)
print(filtrotail)

medias=fuenteDatos.iloc[['mean']]
print("\n")

mediaEdad=medias["edad"]
print(mediaEdad)
