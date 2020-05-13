import os
from dotenv import load_dotenv
import psycopg2
from pdb import set_trace as st
import pandas as pd
import sqlite3

load_dotenv()  # > loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)
cursor = connection.cursor()
print("CURSOR:", cursor)


def query_display(query_file_name):
    query_string = ""
    query_file_path = ("./queries/{}.sql".format(query_file_name))
    with open(query_file_path) as temp_file:
        query_string = temp_file.read()
    return query_string


create_titanic_table_query = query_display("create_table_query")
cursor.execute(create_titanic_table_query)

# result = cursor.fetchall()
# print("RESULT:", type(result))
# print(result)
df = pd.DataFrame(
    {
        "Survived": [True],
        "Pclass": [12],
        "Name": ["naghi"],
        "Sex": ["male"],
        "Siblings/Spouses Aboard": [12],
        "Parents/Children Aboard": [1],
        "Fare": [22.7]
    }
)

connection = sqlite3.connect("./buddymove_holidayiq.sqlite3")
df.to_sql(name='titanic', con=connection, if_exists='replace', index=False)

# df = pd.read_csv("./titanic.csv")
# list(df.to_records(index=False))
st()