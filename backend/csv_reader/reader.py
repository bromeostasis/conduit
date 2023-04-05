import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/ceiling-data.csv')

df = pd.read_csv(filename).fillna('') # TODO: dtypes? maybe don't do here to avoid overwrites.

# Not included: 'Extended Construction Numbers','Look-Up Construction Number','Notes'
ORDERED_CATEGORIES = ['Ceiling type','Deck construction','Attic ventilation','Attic fan','Radiant barrier','Roofing material','Roof color','Insulation','R-value']

def get_next_results(columns_with_selections):

	if columns_with_selections == []:
		return [{'Ceiling type': df['Ceiling type'].unique().tolist()}]

	filtered_df = filter_csv_with_selections(columns_with_selections)
	results = get_next_non_empty_category_or_final_number(filtered_df, columns_with_selections)
	return results

def filter_csv_with_selections(columns_with_selections):
	filtered_df = df
	for selection in columns_with_selections:
		material_category = list(selection.keys())[0]
		material_value = selection[material_category]
		filtered_df = filtered_df.query(f'`{material_category}` == @material_value') # @ is required to deal with quoted '2"" slab'-type values. Prevents creating one big query string.

	return filtered_df

def get_next_non_empty_category_or_final_number(filtered_df, columns_with_selections):
	last_category_queried = list(columns_with_selections[-1].keys())[0]
	column_index = ORDERED_CATEGORIES.index(last_category_queried) + 1
	next_material_values = [''] # empty set
	while next_material_values == [''] and column_index < len(ORDERED_CATEGORIES):
		next_material_category = ORDERED_CATEGORIES[column_index]
		next_material_values = filtered_df[next_material_category].unique().tolist()
		if next_material_values != ['']: # Handling edge case for distinguishing successful R-value find vs. end-of-list
			break
		column_index += 1
	if column_index != len(ORDERED_CATEGORIES):
		results = {}
		results[next_material_category] = next_material_values
		return [results]
	else:
		return {'Extended Construction Numbers': filtered_df['Extended Construction Numbers'].iloc[0]}