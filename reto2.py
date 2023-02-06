#1. Importo a pandas
import pandas as pd

#2.Traigo fuente de datos
Nacional={84,88,84,87,80,83,84,90,78,82,84,90,75,78,98,100,78,65,80,20}
Medellín={90,78,68,87,102,90,80,80,81,78,79,81,83,84.5,90,101,60,70,80,87}

#3. genero los dataframes
dataFrame1=pd.DataFrame(Nacional)
dataFrame2=pd.DataFrame(Medellín)

#4. analisis descriptivo de los datos
analisis1=dataFrame1.describe()
analisis2=dataFrame2.describe()

#5. mostrar resultados 
print(analisis1)
print(analisis2)