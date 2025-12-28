import  sqlite3

## Connedct to DB
connection=sqlite3.connect('student.db')

## Create cursor object to insert record, create table
cursor=connection.cursor()

## Create table
table_info="""
create table IF NOT EXISTS STUDENT \
( \
    NAME    VARCHAR(25), \
    CLASS   VARCHAR(25), \
    SECTIOn VARCHAR(25), \
MARKS INT
)
"""

cursor.execute(table_info)

## Insert records
cursor.execute("INSERT INTO STUDENT VALUES('Rahul','10','A',90)")
cursor.execute("INSERT INTO STUDENT VALUES('Ravi','10','A',80)")
cursor.execute("INSERT INTO STUDENT VALUES('Raj','10','A',70)")
cursor.execute("INSERT INTO STUDENT VALUES('Ravi','10','A',60)")

## Display all records
print("All records:")
data=cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)
## Commit changes
connection.commit()
connection.close()