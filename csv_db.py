import pandas as pd
import sqlite3
import os

def CSV_2_DB():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    database_name = os.path.join(data_dir, 'DataBase.db')
    
    conn = sqlite3.connect(database_name)
    
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(data_dir, filename)
            df = pd.read_csv(csv_path)
            table_name = os.path.splitext(filename)[0]  
            df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()
    print(f"Data from multiple CSV files has been saved to '{database_name}' database.")