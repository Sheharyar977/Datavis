import pandas as pd 
import sqlite3

conn = sqlite3.connect('testMH.db')

df = pd.read_csv('Mental Health Care Health Professional Shortage Areas.csv')

df.to_sql('MH', conn, if_exists='replace', index=False)

conn.close()

