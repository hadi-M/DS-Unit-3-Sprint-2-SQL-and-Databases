# %%<~~~~---- IMPORTS ----~~~~> %% #

import pandas as pd
import sqlite3
import os
from pdb import set_trace as st

# Read sqlite query results into a pandas DataFrame
os.chdir(
	os.path.dirname(
		os.path.abspath(__file__)
		)
	)
con = sqlite3.connect("./rpg_db.sqlite3")


def query_display(query_file_name):
	query_string = ""
	query_file_path = ("./queries/part2/{}.sql".format(query_file_name))

	with open(query_file_path) as temp_file:
		query_string = temp_file.read()

	df = pd.read_sql_query(query_string, con)
	print(
		query_file_name + ":",
		df,
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

# %%$$&& <~~~~---- Q5 ----~~~~> &&$$%% #
# How many Items does each character have? (Return first 20 rows)
query_display("q5")

# %%$$&& <~~~~---- Q6 ----~~~~> &&$$%% #
# How many Weapons does each character have? (Return first 20 rows)
query_display("q6")

# %%$$&& <~~~~---- Q7 ----~~~~> &&$$%% #
# On average, how many Items does each Character have?
query_display("q7")

# %%$$&& <~~~~---- Q8 ----~~~~> &&$$%% #
# On average, how many Weapons does each character have?
query_display("q8")

# %%
con.close()