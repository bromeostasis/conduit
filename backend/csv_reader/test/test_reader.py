from csv_reader.reader import *

def test_get_first_column():
	results = get_next_results([])

	assert results == [{"Ceiling type": ["Ceiling below roof joists", "Ceiling on exposed beams", "Ceiling under attic or attic knee wall"]}]