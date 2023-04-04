import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/ceiling-data.csv')

df = pd.read_csv(filename) # TODO: dtypes? maybe don't do here to avoid overwrites.

ORDERED_COLUMNS = ['Ceiling type','Deck construction','Attic ventilation','Attic fan','Radiant barrier','Roofing material','Roof color','Insulation','R-value','Extended Construction Numbers','Look-Up Construction Number','Notes']

def get_next_results(columns_with_selections):

	if columns_with_selections == []:
		return [{'Ceiling type': df['Ceiling type'].unique().tolist()}]

	filtered_df = filter_csv_with_selections(columns_with_selections)
	next_column = ORDERED_COLUMNS[len(columns_with_selections)] # Since last two columns are extraneous and unselectable, this is safe

	results = {}
	results[next_column] = filtered_df[next_column].unique().tolist()
	return [results]

def filter_csv_with_selections(columns_with_selections):
	first_selection = columns_with_selections[0]
	key = list(first_selection.keys())[0]
	query_string = f'`{key}` == "{first_selection[key]}"'
	# for selection in filter_csv_with_selections:

	return df.query(query_string)
