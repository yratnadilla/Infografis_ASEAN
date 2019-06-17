import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost' ,
        user = 'yourusername',
        passwd = 'yourpassword',
        database = 'world'
    )

query = 'select Name, SurfaceArea from country where Region = "Southeast Asia"'
data = pd.read_sql(query, con= mydb)

plt.figure('Land Ratio of ASEAN Countries')
plt.title('Land Ratio of ASEAN Countries')

color = ['#00796B', '#388E3C', '#689F38', '#AFB42B', '#FBC02D',
        '#FFA000', '#F57C00', '#E64A19', '#5D4037', '#616161', '#455A64']
plt.pie(data['SurfaceArea'], labels=data['Name'], autopct= '%1.1f%%', colors=color)

plt.show()