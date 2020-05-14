
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

con = sqlite3.connect("./rpg_db.sqlite3")
query_string = "SELECT * FROM armory_item"
df = pd.read_sql_query(query_string, con)


connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database  # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.armory_item  # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

# df = pd.read_csv("./titanic.csv")
collection.insert_many(df.to_dict(orient='records'))
# print("DOCS:", collection.count_documents({}))
# print(collection.count_documents({"name": "Pikachu"}))