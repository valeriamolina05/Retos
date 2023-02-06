#1. Importo a pandas
import pandas as pd

#2.Traigo fuente de datos
Paciente1={45,280,124,250,79,300,26,59,200,60,210,39,110,59,69,54}
Paciente2={120,125,122,125,119,121,120,119,120,124,125,120,117,130,127,125}


#3. genero los dataframes
dataFrame1=pd.DataFrame(Paciente1)
dataFrame2=pd.DataFrame(Paciente2)

#4. analisis descriptivo de los datos
analisis1=dataFrame1.describe()
analisis2=dataFrame2.describe()

#5. mostrar resultados 
print(analisis1)
print(analisis2)
