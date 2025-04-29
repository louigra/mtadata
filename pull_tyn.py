import json
import sqlite3
import pandas as pd

with open('tynadata.json', 'r') as f:
    data = json.load(f)
    
df = pd.DataFrame(data)
conn = sqlite3.connect('tynadata.db')
df.to_sql('tynadata', conn, if_exists='replace', index=False)
conn
print("data loaded to sqlite3 database tynadata.db")