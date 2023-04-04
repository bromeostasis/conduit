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