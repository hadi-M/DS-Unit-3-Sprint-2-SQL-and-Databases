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

con = None
# if db file is not already filled with data, fill it:
if "buddymove_holidayiq.sqlite3" not in os.listdir():
	con = sqlite3.connect("./buddymove_holidayiq.sqlite3")
	pd.read_csv("./buddymove_holidayiq.csv").to_sql("review", con=con)

else:
	con = sqlite3.connect("./buddymove_holidayiq.sqlite3")


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
# Count how many rows you have - it should be 249! yep 249
query_display("q1")

# %%$$&& <~~~~---- Q2 ----~~~~> &&$$%% #
# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category? 78
query_display("q2")

# %%$$&& <~~~~---- Q3 ----~~~~> &&$$%% #
# (Stretch) What are the average number of reviews for each category?
query_display("q3")