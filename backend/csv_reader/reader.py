import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/ceiling-data.csv')

df = pd.read_csv(filename) # TODO: dtypes? maybe don't do here to avoid overwrites.

def get_next_results(columns_with_selections):

	if columns_with_selections == []:
		return [{'Ceiling type': df['Ceiling type'].unique().tolist()}]