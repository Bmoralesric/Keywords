#pip install pytrends 
#pip install pandasql 
#pip install pandas
#pip install matplopiptlib 
import pytrends
import csv
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
from datetime import date
from pandasql import sqldf
from pytrends.request import TrendReq
pysqldf = lambda q: sqldf(q, globals())

from pytrends.request import TrendReq
import pandas as pd
import time
from datetime import date
import plotly.express as px

startTime = time.time()
pytrend = TrendReq(hl='es-MX', tz=360)
today = date.today()
colnames = ["keywords"]
df = pd.read_csv("C:/Users/HP/Desktop/Keywords CV/Keywords.txt", names=colnames)
df2 = df["keywords"].values.tolist()


dataset = []

for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe= '2020-01-01' + ' ' + '2020-12-31',
     geo='MX-JAL')
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset.append(data)

result = pd.concat(dataset, axis=1)
print(result.head())


 
fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('AS')
#Colocamos una etiqueta en el eje X
ax.set_title('Cantidad de Ventas por Pais')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.bar(result.index, result)
plt.savefig('barras_simple.png')
#Finalmente mostramos la grafica con el metodo show()
plt.show()
