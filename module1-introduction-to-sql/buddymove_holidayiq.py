# %%<~~~~---- IMPORTS ----~~~~> %% #

import pandas as pd
import sqlite3
import os
from pdb import set_trace as st

# Read sqlite query results into a pandas DataFrame
# os.join.path()
con = sqlite3.connect("./buddymove_holidayiq.sqlite3")
if "buddymove_holidayiq.sqlite3" not in os.listdir():
    pd.read_csv("./buddymove_holidayiq.csv").to_sql("review", con=con)


def query_display(query_file_name):
	query_string = ""
	with open("./queries/part2/{}.sql".format(query_file_name)) as temp_file:
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