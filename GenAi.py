from langchain_community.utilities.sql_database import SQLDatabase
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, create_sql_query_chain
import os
import streamlit as st
import re

def GenAi(questions):
    llm = ChatGroq(model="llama3-70b-8192", api_key= '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')
    db = SQLDatabase.from_uri("sqlite:///F:\works\A-important\A-neurals\Thendral-sir-tutorials\chat-with-databases\data\DataBase.db")
    chain = create_sql_query_chain(llm, db)
    sql_query = chain.invoke({'question': questions})
    final = re.sub(r'^SQLQuery:\s*', '', sql_query, flags=re.IGNORECASE).strip()
    print("===========>", final)
    result = db.run(final)
    answer_prompt = PromptTemplate.from_template(
        """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply to give to user, dont gice anything else except the answer

    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: """
    
    )

    llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
    llm = LLMChain(llm=llm_model, prompt=answer_prompt)
    ans = llm(inputs={"question": questions, "query": sql_query, "result": result})
    return ans["text"]
print(GenAi(""))