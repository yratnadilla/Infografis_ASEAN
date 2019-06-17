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

plt.bar(data['Name'], data['GNP'])

for x, y in zip(data['Name'], data['GNP']):
    label = "{:,}".format(int(y))
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=6)

plt.xlabel('Countries')
plt.ylabel('GNP (in US$)')
plt.xticks(rotation=45)
plt.show()