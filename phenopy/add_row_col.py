import pandas as pd
from string import letters

def  add_row_col(data,
	well_name = "well",
	row_name = "row",
	col_name = "column"):

	"""
	Function to add numeric well and column values for inputted alpha-numeric well IDs.
	Input dataframe, will append two additional columns  
	----------------
	  arguments:
	- data      : pd.Dataframe, dataframe to be annotated
	- well_name : string, column within data that contains well IDs
	- row_name  : string, name of column to contains row values
	- col_name  : string, name of column to contain column values
	----------------
	"""

	# create function like R's match()
	match = lambda a, b: [b.index(x) if x in b else None for x in a]

	wells = data[well_name]
	row_letters = [x[0] for x in wells] # extract row letters from input well column
	
	row_ = pd.Series(match(row_letters, list(letters[:26])))
	row_ = row_ + 1
	column_ = pd.Series([x[1:] for x in wells])
	column_ = column_.astype(int) # force column to an integer

	data[row_name] = row_
	data[col_name] = column_

	return(data)