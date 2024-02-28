# test my code
from src import my_code as lib_logic

def test_addition():
	output = lib_logic.add(5,2)
	if output < 10:
		status = 'SUCCESS'
	else:
		status = 'FAILURE'
	assert status == 'SUCCESS'
