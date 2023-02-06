import pandas as pd

tabla=pd.read_csv("./empleados.csv")

print(tabla["salario"].to_string())

