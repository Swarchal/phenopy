import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from string import uppercase, letters

def read_map(data, p_map,
    col_name = 'header',
	well_name = 'well',
	verbose = False):

	"""
	annotates pd.dataframe with labels from an external .csv file
	in the layout of a plate
	---------------
	  arguments :
	- data      : pd.Dataframe, dataframe to be annotated
	- p_map     : array of annotations
	- col_name  : string, what to call the column of annotations
	- well_name : string, name of column within 'data' containing wellIDs
	- verbose   : boolean, if True will add numeric values for row and column to data
	--------------
	"""

	# create equivalent of R's match function
	# remove '+1' to make zero-indexed if needed
	match = lambda a, b: [ b.index(x) if x in b else None for x in a ]

	# select column of well labels
	wells = data[well_name]
	row_letters =  [x[0] for x in wells]

	#  add 'column' and 'row' columns to pd.df 'data'
	row_ = Series(match(row_letters, list(letters[:26])))
	column_ = Series([x[1:] for x in wells])
	column_ = column_.astype(int)
	column_ = column_ - 1

	data['row'] = row_
	data['column'] = column_

	data[col_name] = np.nan

	# * assign to 'col_name' values from 'map' that match row and column
	# from 'data'
	p_map = np.array(p_map) # force p_map into an array

	for i in xrange(len(data.index)):
		data[col_name].iloc[i] = p_map[data['row'].iloc[i], data['column'].iloc[i]]
	
	# drop 'column' and 'row' columns
	if verbose == False:
		data.drop('row', axis=1, inplace = True)
		data.drop('column', axis = 1, inplace = True)

	return(data)