
import pymongo
import os
from dotenv import load_dotenv
from pdb import set_trace as st
import pandas as pd
import sqlite3


load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

sqlite_con = sqlite3.connect("./rpg_db.sqlite3")
query_string = "SELECT * FROM charactercreator_mage"
df = pd.read_sql_query(query_string, sqlite_con)


pymongo_connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

print("URI:", pymongo_connection_uri)

client = pymongo.MongoClient(pymongo_connection_uri)

db = client["rpg_db"]

collection = db["charactercreator_mage"]

print(db.list_collection_names())

collection.insert_many(df.to_dict(orient='records'))