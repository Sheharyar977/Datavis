import pandas as pd 
import sqlite3

conn = sqlite3.connect('testMH.db')

df = pd.read_csv('Mental Health Care Health Professional Shortage Areas.csv')

df.to_sql('MH2', conn, if_exists='replace', index=False)

conn.execute('''
CREATE TABLE MH2_temp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Location TEXT,
    Total_Mental_Health_Care_HPSA_Designations INTEGER,
    Population_of_Designated_HPSAs REAL,
    Percent_of_Need_Met REAL,
    Practitioners_Needed_to_Remove_HPSA_Designation REAL
)
''')

conn.execute('''
INSERT INTO MH2_temp (Location, Total_Mental_Health_Care_HPSA_Designations, Population_of_Designated_HPSAs, Percent_of_Need_Met, Practitioners_Needed_to_Remove_HPSA_Designation)
SELECT "Location", "Total Mental Health Care HPSA Designations", "Population of Designated HPSAs", "Percent of Need Met", "Practitioners Needed to Remove HPSA Designation" 
FROM MH2
''')

conn.execute('DROP TABLE MH2')


conn.execute('ALTER TABLE MH2_temp RENAME TO MH2')

conn.commit()
conn.close()