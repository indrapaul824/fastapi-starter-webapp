# Arcane incantation to print all the other targets, from https://stackoverflow.com/a/26339924
help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

# Install exact Python versions
conda-update:
	conda env update --prune -f environment.yml

# Compile and install exact pip packages
pip-tools:
	pip install pip-tools
	pip-compile requirements.in
	pip-sync requirements.txt

# Run developement server from root directory
run-app:
	uvicorn app.main:app --reload --host=0.0.0.0 --port=8000 
