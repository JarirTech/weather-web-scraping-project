import sqlite3
import pandas as pd


# read cleaned csv data

df = pd.read_csv('./cleaned_weather_data.csv')
#print(df.head())


conn = sqlite3.connect("../weather_data.db")
df.to_sql("weather_data", conn, if_exists="replace", index=False)

conn.close()

