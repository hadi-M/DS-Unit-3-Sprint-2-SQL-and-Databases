# %%<~~~~---- IMPORTS ----~~~~> %% #

import pandas as pd
import sqlite3
import os
from pdb import set_trace as st

# Read sqlite query results into a pandas DataFrame
# os.join.path()
con = sqlite3.connect("./rpg_db.sqlite3")


def query_display(query_file_name):
	query_string = ""
	with open("./queries/{}.sql".format(query_file_name)) as temp_file:
		query_string = temp_file.read()

	df = pd.read_sql_query(query_string, con)
	print(
		query_file_name + ":",
		df.head(),
		sep="\n",
		end="\n"+"-"*20+"\n\n"
	)

	return df


# %%$$&& <~~~~---- Q1 ----~~~~> &&$$%% #
# How many total Characters are there? 302
query_display("q1")

# %%$$&& <~~~~---- Q2 ----~~~~> &&$$%% #
# How many of each specific subclass?
query_display("q2")

# %%$$&& <~~~~---- Q3 ----~~~~> &&$$%% #
# How many total Items? 898
query_display("q3")

# %%$$&& <~~~~---- Q4 ----~~~~> &&$$%% #
# How many of the Items are weapons? How many are not?
query_display("q4")

# %%
con.close()