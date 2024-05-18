import pandas as pd

import sqlite3

import os

database_name = r'F:\works\A-important\A-neurals\Thendral-sir-tutorials\chat-with-databases\data\DataBase.db'
conn = sqlite3.connect(database_name)
csv_dir = r'F:\works\A-important\A-neurals\Thendral-sir-tutorials\chat-with-databases\data'
for filename in os.listdir(csv_dir):
    if filename.endswith('.csv'):
        csv_path = os.path.join(csv_dir, filename)
        df = pd.read_csv(csv_path)
        table_name = os.path.splitext(filename)[0]  
        df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.commit()
conn.close()
print(f"Data from multiple CSV files has been saved to '{database_name}' database.")
