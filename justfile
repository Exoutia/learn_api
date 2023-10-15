# Default
just:
  just --list

bpython:
  source ~/.cache/pypoetry/virtualenvs/learn-api-UfH_R79d-py3.11/bin/activate  && python -m bpython

app_run:
  source ~/.cache/pypoetry/virtualenvs/learn-api-UfH_R79d-py3.11/bin/activate  && uvicorn app.main:app --reload 
	
