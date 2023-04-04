import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/ceiling-data.csv')

df = pd.read_csv(filename).fillna('') # TODO: dtypes? maybe don't do here to avoid overwrites.

# Not included: 'Extended Construction Numbers','Look-Up Construction Number','Notes'
ORDERED_COLUMNS = ['Ceiling type','Deck construction','Attic ventilation','Attic fan','Radiant barrier','Roofing material','Roof color','Insulation','R-value']

def get_next_results(columns_with_selections):

	if columns_with_selections == []:
		return [{'Ceiling type': df['Ceiling type'].unique().tolist()}]

	filtered_df = filter_csv_with_selections(columns_with_selections)
	results = get_next_non_empty_column_or_final_number(filtered_df, columns_with_selections)
	return results

def filter_csv_with_selections(columns_with_selections):
	first_selection = columns_with_selections[0]
	key = list(first_selection.keys())[0]
	query_string = f'`{key}` == "{first_selection[key]}"'
	for selection in columns_with_selections:
		row = list(selection.keys())[0]
		if row != key: # Skip first key
			query_string += f' & `{row}` == "{selection[row]}"'

	return df.query(query_string)

def get_next_non_empty_column_or_final_number(filtered_df, columns_with_selections):
	last_column_queried = list(columns_with_selections[-1].keys())[0]
	column_index = ORDERED_COLUMNS.index(last_column_queried) + 1
	next_values = []
	while (len(next_values) == 0 or next_values == ['']) and column_index < len(ORDERED_COLUMNS):
		next_column = ORDERED_COLUMNS[column_index] # Since last two columns are extraneous and unselectable, this is safe
		next_values = filtered_df[next_column].unique().tolist()
		column_index += 1
	if column_index != len(ORDERED_COLUMNS):
		results = {}
		results[next_column] = next_values
		return [results]
	else:
		return filtered_df['Extended Construction Numbers'].iloc[0]