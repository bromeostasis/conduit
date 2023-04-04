from csv_reader.reader import *

def test_get_first_column():
	results = get_next_results([])

	assert results == [{"Ceiling type": ["Ceiling below roof joists", "Ceiling on exposed beams", "Ceiling under attic or attic knee wall"]}]

def test_get_second_column_simple():
	results = get_next_results([{'Ceiling type': 'Ceiling on exposed beams'}])

	assert results == [
		{
			'Deck construction': [
				'1.5" wood',
				'2" cement fiber slab',
				'3" cement fiber slab'
			]
		}
	]

def test_get_column_with_blanks():
	results = get_next_results([{'Ceiling type': 'Ceiling below roof joists'}])

	assert results == [
		{
			'Roofing material': [
				'Asphalt shingles',
				'Membrane',
				'Metal',
				'Tar and gravel',
				'Tile',
				'Wood shakes'
			]
		}
	]

def test_get_column_with_multiple_filters():
	results = get_next_results([{'Ceiling type': 'Ceiling below roof joists'}, {'Roofing material': 'Tar and gravel'}])

	assert results == [
		{
			'Roof color': [
				'Dark',
				'Light'
			]
		}
	]

def test_get_final_result():
	results = get_next_results([
		{'Ceiling type': "Ceiling under attic or attic knee wall"},
		{'Attic ventilation': "FHA vented"},
		{'Attic fan': "Yes"},
		{'Roofing material': "Metal"},
		{'Roof color': "Light"},
		{'R-value': "R-19"},
	])

	assert results == {'Extended Construction Numbers': '16DF-19 ml'}

def test_get_r_value():
	results = get_next_results([
		{'Ceiling type': 'Ceiling below roof joists'},
		{'Roofing material': 'Tar and gravel'},
		{'Roof color': 'Dark'},
		{'Insulation': 'Blanket or loose fill'}
	])

	assert results == [{'R-value': ['R-11','R-13','R-15','R-19','R-21','R-30','R-38']}]


def test_empty_r_value():
	results = get_next_results([
		{'Ceiling type': 'Ceiling below roof joists'},
		{'Roofing material': 'Asphalt shingles'},
		{'Roof color': 'Dark'},
		{'Insulation': 'None'}
	])

	assert results == {'Extended Construction Numbers': '18A-0 ad'}

def test_quoted_values():
	results = get_next_results([
		{'Ceiling type': "Ceiling on exposed beams"},
		{'Deck construction': '1.5" wood'},
		{'Roofing material': "Tar and gravel"},
	])

	assert results == [{'Roof color': ['Dark', 'Light']}]

