# Default
just:
  just --list

bpython:
  source $(poetry env info --path)/bin/activate  && python -m bpython

app_run:
  source $(poetry env info --path)/bin/activate  && uvicorn app.main:app --reload 
	
nvim:
  source $(poetry env info --path)/bin/activate  && nvim
