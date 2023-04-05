import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/ceiling-data.csv')

df = pd.read_csv(filename).fillna('') # TODO: dtypes? maybe don't do here to avoid overwrites.

# Not included: 'Extended Construction Numbers','Look-Up Construction Number','Notes'
ORDERED_CATEGORIES = ['Ceiling type','Deck construction','Attic ventilation','Attic fan','Radiant barrier','Roofing material','Roof color','Insulation','R-value']

def get_next_results(material_selections):
	if material_selections == []:
		return [{'Ceiling type': df['Ceiling type'].unique().tolist()}]

	filtered_df = filter_materials_with_selections(material_selections)
	results = get_next_non_empty_category_or_final_number(filtered_df, material_selections)
	return results

def filter_materials_with_selections(material_selections):
	filtered_df = df
	for material_selection in material_selections:
		material_category = get_first_dict_key(material_selection)
		material_value = material_selection[material_category]
		filtered_df = filtered_df.query(f'`{material_category}` == @material_value') # @ is required to deal with quoted '2"" slab'-type values. Prevents creating one big query string.

	return filtered_df

def get_next_non_empty_category_or_final_number(filtered_df, material_selections):
	last_category_queried = get_first_dict_key(material_selections[-1])
	ordered_category_index = ORDERED_CATEGORIES.index(last_category_queried) + 1
	next_material_values = [''] # empty set
	while next_material_values == [''] and ordered_category_index < len(ORDERED_CATEGORIES):
		next_material_category = ORDERED_CATEGORIES[ordered_category_index]
		next_material_values = filtered_df[next_material_category].unique().tolist()
		if next_material_values != ['']: # Handling edge case for distinguishing successful R-value find vs. end-of-list
			break
		ordered_category_index += 1

	if ordered_category_index != len(ORDERED_CATEGORIES):
		results = {}
		results[next_material_category] = next_material_values
		return [results]
	else:
		return {'Extended Construction Numbers': filtered_df['Extended Construction Numbers'].iloc[0]}

def get_first_dict_key(dictionary):
	return list(dictionary.keys())[0]