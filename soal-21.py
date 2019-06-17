import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost' ,
        user = 'yourusername',
        passwd = 'yourpassword',
        database = 'world'
    )

query = 'select Name, Population from country where Region = "Southeast Asia" order by Population desc'
data = pd.read_sql(query, con= mydb)

plt.style.use('seaborn')
plt.figure('Population of ASEAN Countries')
plt.title('Population of ASEAN Countries')

color = ['#00796B', '#388E3C', '#689F38', '#AFB42B', '#FBC02D',
        '#FFA000', '#F57C00', '#E64A19', '#5D4037', '#616161', '#455A64']
plt.bar(data['Name'], data['Population'], color=color)

for x,y in zip(data['Name'], data['Population']):
    label = "{:,}".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=6)

plt.xlabel('Countries')
plt.ylabel('Population (in hundred million)')
plt.xticks(rotation=45)

plt.show()