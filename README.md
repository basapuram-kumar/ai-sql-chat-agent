# ai-sql-chat-agent
AI-powered SQL agent for conversational database interactions. Chat with MySQL and SQLite databases using natural language powered by LangChain, Groq, and Streamlit.

## Features
- 💬 Natural language to SQL conversion
- 🗄️ Support for MySQL and SQLite
- 🤖 AI-powered query generation
- 📊 Interactive chat interface
- 🔄 Real-time schema refresh

  
## Set Up prerequisites


###  Create virtual environment
```
python3.11 -m venv myenv
```

### Activate virtual environment
```
source myenv/bin/activate
```

###  Verify Python Version
Confirm you're using Python 3.11:
```
python -V
```
Expected output: Python 3.11.13

### Install Dependencies
Install all required Python packages:
```
pip install -r requirements.txt
```

# Run sequel chat agent Application
Launch the Streamlit application:
```
streamlit run ollamaDemo.py
```
Response
```
➜ streamlit run mysql_app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.29.242:8501
```

# Screenshots
### Initial UI Screen
<img width="1494" height="341" alt="Screenshot 2025-12-29 at 04 58 08" src="https://github.com/user-attachments/assets/34ece0b0-444a-458b-9057-cacd19b8c3c2" />

### Enter the Groq API KEY - Search on SQLITE3 database

<img width="1460" height="697" alt="Screenshot 2025-12-29 at 04 58 29" src="https://github.com/user-attachments/assets/c49a21fe-2495-4184-904c-50d61a7ef9b3" />

### Ask queries to chatbot
#### Default search after entering Groq Key
<img width="1469" height="775" alt="Screenshot 2025-12-29 at 05 00 22" src="https://github.com/user-attachments/assets/1a661b37-b4c7-4123-b8e1-a9e1dbdc12da" />

#### Asked a query
<img width="1503" height="714" alt="Screenshot 2025-12-29 at 05 01 07" src="https://github.com/user-attachments/assets/60d86690-c680-4040-8ed0-aeea68744884" />

## Connect to MySQL Database
### Setup test local instance of mysql running on docker contianer.

#### Pull mysql Image
```
docker pull mysql:8.0.42
```
#### Start mysql container
```
docker run -d \
  --name mysql-80_42 \
  -e MYSQL_ROOT_PASSWORD=test@01 \
  -p 3306:3306 \
  mysql:8.0.42
```
After up and Running, login to contianer
```
docker exec -it mysql-80_42 mysql -uroot -ptest@01
```

insert sample data
```
create database student;
use student;


INSERT INTO STUDENT VALUES('Rahul','10','A',90)
INSERT INTO STUDENT VALUES('Ravi','10','A',80)
INSERT INTO STUDENT VALUES('Raj','10','A',70)
INSERT INTO STUDENT VALUES('Ravi','10','A',60)
```

Connect from App
Choose "Connect to your MySQL DB" from the list of DB's on top side, and provide details

<img width="1494" height="700" alt="Screenshot 2025-12-29 at 05 08 08" src="https://github.com/user-attachments/assets/f43ba002-19cf-40b2-84ce-f5a95c3faf99" />

And enter connection details
<img width="1495" height="791" alt="Screenshot 2025-12-29 at 05 08 56" src="https://github.com/user-attachments/assets/e74752ea-bb7c-442c-a838-3f7281805976" />

### Ask sample Queries to fetch details  from mysql
<img width="1501" height="814" alt="Screenshot 2025-12-29 at 05 12 19" src="https://github.com/user-attachments/assets/738c9a08-22b8-432a-ae73-ad008000c209" />


Tags

langchain, sql, chatbot, groq, streamlit, database, ai-agent, natural-language, llm, python, mysql, sqlite
