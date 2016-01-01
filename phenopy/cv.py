#!/usr/bin/env python

from __future__ import division
import numpy as np
import pandas as pd

def cv(x):
	"coefficient of variation"
	sd = np.std(x)
	mean = np.mean(x)
	cv = (sd / mean) * 100
	return cv


def cv_check(data, group):
	"""
	Calculates the coefficient of variation across groups
	------------------------------------------------------
	data  :   DataFrame
	group :   name or index of column to group data
	"""

	# check if argument is a string or column indices
	if type(group) is str:
		data_grouped = data.groupby(group)
	elif type(group) is int:
		data_grouped = data.groupby(data.ix[:,group])

	# use .apply() to use cv function on grouped object
	cv_data = data_grouped.apply(cv)

	return cv_data


# checks
df = pd.DataFrame({
  'v1':  [1,3,5,7,8,3,5,4,4,5,7,9],
  'v2':  [4,3,3,3,4,6,3,4,3,3,3,5],
  'by1': ['a', 'a', 'b', 'a', 'a', 'b', 'b', 'a', 'b', 'a', 'b', 'a']
})

print cv_check(df.ix[:,0], 'by1')