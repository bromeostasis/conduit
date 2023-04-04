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
	filter_value = first_selection[key]
	filtered_df = df.query(f'`{key}` == @filter_value') # @ required to deal with quoted '2"" slab'-type values. Prevents creating one big query string.
	for selection in columns_with_selections:
		row = list(selection.keys())[0]
		if row != key: # Skip first key
			filter_value = selection[row]
			filtered_df = filtered_df.query(f'`{row}` == @filter_value')

	return filtered_df

def get_next_non_empty_column_or_final_number(filtered_df, columns_with_selections):
	last_column_queried = list(columns_with_selections[-1].keys())[0]
	column_index = ORDERED_COLUMNS.index(last_column_queried) + 1
	next_values = [''] # empty set
	while next_values == [''] and column_index < len(ORDERED_COLUMNS):
		next_column = ORDERED_COLUMNS[column_index]
		next_values = filtered_df[next_column].unique().tolist()
		if next_values == [''] or column_index + 1 != len(ORDERED_COLUMNS): # TODO: UGGGly edge case for distinguishing successful R-value find vs. end-of-list
			column_index += 1
	if column_index != len(ORDERED_COLUMNS):
		results = {}
		results[next_column] = next_values
		return [results]
	else:
		return {'Extended Construction Numbers': filtered_df['Extended Construction Numbers'].iloc[0]}