import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost' ,
        user = 'yourusername',
        passwd = 'yourpassword',
        database = 'world'
    )

query = 'select Name, GNP from country where Region = "Southeast Asia" order by GNP desc'
data = pd.read_sql(query, con= mydb)

plt.style.use('seaborn')
plt.figure('GNP of ASEAN Countries')
plt.title('GNP of ASEAN Countries')

color = ['#00796B', '#388E3C', '#689F38', '#AFB42B', '#FBC02D',
        '#FFA000', '#F57C00', '#E64A19', '#5D4037', '#616161', '#455A64']
plt.bar(data['Name'], data['GNP'], color=color)

for x, y in zip(data['Name'], data['GNP']):
    label = "{:,}".format(int(y))
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=6)

plt.xlabel('Countries')
plt.ylabel('GNP (in US$)')
plt.xticks(rotation=45)
plt.show()