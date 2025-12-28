## Reference - https://docs.langchain.com/oss/python/langchain/sql-agent#huggingface
import streamlit as st
from pathlib import Path
from langchain_classic.agents import create_sql_agent
from langchain_classic.sql_database import SQLDatabase
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.callbacks import StreamlitCallbackHandler
from langchain_classic.agents.agent_toolkits import  SQLDatabaseToolkit
from sqlalchemy import create_engine
from urllib.parse import quote_plus

import  sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="LangChain: Chat with sequel DB", page_icon=":robot:")
st.title("LangChain: Chat with sequel DB")

# INJECTION_WARNING = """
# SQL agent can be volunerable to prompt injection, Use a DB Role with limited permissions
# """

LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"

radio_opt=["Use Sqlite3 DB - student.db","Connect to your MySQL DB"]
selected_db=st.sidebar.radio(label="Select the DB which you wanted to Chat", options=radio_opt)

if radio_opt.index(selected_db)==1:
    db_uri=MYSQL
    mysqldb_host=st.sidebar.text_input("Enter your MySQL DB Host")
    mysqldb_port = st.sidebar.text_input("Port", value="3306")
    mysqldb_user=st.sidebar.text_input("Enter your MySQL DB Username")
    mysqldb_password=st.sidebar.text_input("Enter your MySQL DB Password",type="password")
    mysqldb_db=st.sidebar.text_input("Enter your MySQL DB Name")
else:
    db_uri=LOCALDB



if  not db_uri:
    st.info("Please select a DB information and uri")

# if not api_key:
#     st.info("Please add the groq api key")

### LLM model
# llm=ChatGroq(model="llama-3.1-8b-instant", groq_api_key=api_key, streaming=True)

api_key=st.sidebar.text_input(label="GROQ API key:",type="password")

if not api_key:
    st.info("Please enter your GROQ API key")
    st.stop()

llm=ChatGroq(api_key=api_key,model_name="qwen/qwen3-32b",streaming=True)

@st.cache_resource(ttl="60")
def configure_db(db_uri, mysql_host=None,mysql_port=None, mysql_user=None,mysql_password=None, mysql_db=None):
    if db_uri==LOCALDB:
        db_file_path=(Path(__file__).parent/"student.db").absolute()
        print(db_file_path)
        creator= lambda : sqlite3.connect(f"file:{db_file_path}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri==MYSQL:
        if not (mysql_host and mysql_port and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all the MySQL Connection details")
            st.stop()
        encoded_user = quote_plus(mysql_user)
        encoded_password = quote_plus(mysql_password)

        connection_string = f"mysql+mysqlconnector://{encoded_user}:{encoded_password}@{mysql_host}:{mysql_port}/{mysql_db}"

        return SQLDatabase(create_engine(connection_string))


if db_uri==MYSQL:
    db=configure_db(db_uri,mysqldb_host,mysqldb_port,mysqldb_user,mysqldb_password,mysqldb_db)
else:
    db=configure_db(db_uri)

## Toolkit usage
toolkit=SQLDatabaseToolkit(db=db, llm=llm)

agent=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"]=[
        {"role":"assistant","content":"How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message("role").write(msg["content"])

user_query=st.chat_input(placeholder="Ask anything from SQL DB")

if user_query:
    st.session_state.messages.append({"role":"user","content":user_query})
    st.chat_message("user").write(user_query)

with st.chat_message("assistant"):
    streamlit_callback=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
    response=agent.run(user_query,callbacks=[streamlit_callback])
    st.session_state.messages.append({"role":"assistant","content":response})
    st.write(response)

# Add some example queries in the main area
with st.expander("💡 Example Queries"):
    st.markdown("""
    Try asking questions like:
    - "How many records are in each table?"
    - "Show me the first 5 rows from the students table"
    - "What is the average age of students?"
    - "List all tables in the database"
    - "Show me students with grade A"
    - "Count how many students are in each grade"
    """)
