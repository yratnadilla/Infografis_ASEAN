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

plt.bar(data['Name'], data['Population'])

for x,y in zip(data['Name'], data['Population']):
    label = "{:,}".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,5), ha='center', fontsize=6)

plt.xlabel('Countries')
plt.ylabel('Population (in hundred million)')
plt.xticks(rotation=45)

plt.show()