import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost' ,
        user = 'yourusername',
        passwd = 'yourpassword',
        database = 'world'
    )

query = 'select Name, Population from country where Region = "Southeast Asia"'
data = pd.read_sql(query, con= mydb)

plt.figure('Population Ratio of ASEAN Countries')
plt.title('Population Ratio of ASEAN Countries')

plt.pie(data['Population'], labels=data['Name'], autopct= '%1.1f%%')

plt.show()