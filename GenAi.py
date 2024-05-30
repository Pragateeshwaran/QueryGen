from langchain_community.utilities.sql_database import SQLDatabase
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, create_sql_query_chain
import re

def extract_sql_query(template):
    answer_prompt = PromptTemplate.from_template(
        """you are a Sql_Query Extractor from noise string. Given the Noisy Sql template from that Exctract SQL query alone Dont give anything else. Just extract the Query and give it as an answer.

    Noisy_query: {template}

    Answer: """
    )

    llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
    llm = LLMChain(llm=llm_model, prompt=answer_prompt)
    ans = llm(inputs={"template": template})
    print(ans["text"])
    return ans["text"]

def Gen_Ai(questions):
    llm = ChatGroq(model="llama3-70b-8192", api_key='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')
    db = SQLDatabase.from_uri("sqlite:///F:\works\A-important\A-neurals\QueryGen\data\DataBase.db")
    chain = create_sql_query_chain(llm, db)
    sql_query = chain.invoke({'question': questions})
    final = extract_sql_query(sql_query)
    result = db.run(final)

    answer_prompt = PromptTemplate.from_template(
        """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply with proper structure to give to the user, don't give anything else except the answer.

    Question: {question}
    SQL Query: {query}
    SQL Result: {result}

    Answer: """
    )

    llm_model = ChatGroq(model="llama3-70b-8192", api_key='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')
    llm = LLMChain(llm=llm_model, prompt=answer_prompt)
    ans = llm(inputs={"question": questions, "query": sql_query, "result": result})
    return ans["text"], final