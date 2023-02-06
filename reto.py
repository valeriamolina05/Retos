import pandas as pd
 

fuenteDatos=pd.read_csv("./empleados.csv")

filtrohead=fuenteDatos.head(50)
print(filtrohead) 

filtrohead2=fuenteDatos.head(50)["salario"]
print ("\n")
print(filtrohead2)

media=fuenteDatos.describe()
print(media)
print("\n")

filtroIloc=fuenteDatos.iloc[[100,200,300,400]]
print ("\n")
print(filtroIloc)

filtrotail=fuenteDatos.tail(3)[["nombres", "salario"]] 
print ("\n")
print(filtrotail)

