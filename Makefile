check:
	black . --line-length 120
	flake8 
	pytype --keep-going 

