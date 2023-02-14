import pandas as pd 

data=pd.read_csv("./empleados.csv")

#1. Filtrar empleados que solo sean analistas 1
filtro1=data[data["cargo"]=="analista1"]
print(filtro1)

#2. Filtrar empleados que solo sean analistas 2
filtro2=data[data["cargo"]=="analista2"]
print(filtro2)

#3. Filtrar empleados en general que tengan menos de 30 años
filtro3=data[data["edad"]<30]
print(filtro3)

#4. Filtrar empleados en general que tengan mas de 50 años
filtro4=data[data["edad"]>50]
print(filtro4)

#5. ¿Cuál es el promedio de salario de un analista 1?
filtro5=filtro1["salario"].mean()
print(filtro5)

#6. ¿Cuál es el promedio de salario de un analista 2?
filtro6=filtro2["salario"].mean()
print(filtro6)

#7. Filtrar empleados cuyo porcentaje de deducción sea mayor al 10%
filtro7=data[data["porcentajeDeduccion"]>10]
print(filtro7)

#8. Cambiar todos los datos nan por el valor 0
filtro8=data.fillna(0)
print(filtro8)


#9. Cambiar los nan de nombres por la palabra default, los nan de cargo por el mensaje sin cargo y edad por 0
filtro9=data.fillna({"nombres":"Default", "cargo":"Sin cargo", "edad":0})
print(filtro9)





