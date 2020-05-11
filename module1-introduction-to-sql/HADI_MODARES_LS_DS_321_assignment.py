import pandas as pd
import sqlite3
import os
from pdb import set_trace as st

# Read sqlite query results into a pandas DataFrame
# os.join.path()
con = sqlite3.connect("./rpg_db.sqlite3")


# How many total Characters are there? 302
q1 = """
select
count(distinct character_id) as "total_unique_character"
from
charactercreator_character
"""

df1 = pd.read_sql_query(q1, con)

# Verify that result of SQL query is stored in the dataframe
print(df1.head())

con.close()
