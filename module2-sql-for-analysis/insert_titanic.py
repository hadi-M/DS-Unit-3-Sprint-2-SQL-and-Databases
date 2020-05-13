import os
from dotenv import load_dotenv
from pdb import set_trace as st
import pandas as pd
from sqlalchemy import create_engine


load_dotenv()  # > loads contents of the .env file into the script's environment
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

postgres_url = r'postgresql://{}:{}@{}:5432/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

engine = create_engine(postgres_url, echo=False)

df = pd.read_csv("./titanic.csv")
df["Survived"] = df["Survived"].astype("boolean")
df.to_sql(name='titanic_temp2', con=engine, if_exists='replace', index=False, method='multi')