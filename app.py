import os
import sqlite3
import pandas as pd
from csv_db import CSV_2_DB
from GenAi import Gen_Ai
import streamlit as st

def main():
    st.title("CSV to SQLite Database")

    with st.sidebar:
        st.subheader("Upload CSV Files")
        uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)
        if uploaded_files:
            st.write(":green[DB created]")
   
    # col1, col2, col3 = st.columns([1, 2, 1])
    
    user_query = st.text_input("Enter your query", key="query_input")

    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_path = os.path.join(r"F:\works\A-important\A-neurals\QueryGen\data", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        CSV_2_DB()
        

    if user_query:
        try:
            result, query = Gen_Ai(user_query)
            st.write(f"SQL Query : {query}")
            st.write(f":green[{result}]")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()