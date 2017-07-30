ENVIRONMENT := _env/


$(ENVIRONMENT):
	python3 -m venv "$@"

default: help


clean:
	rm -rf "$(ENVIRONMENT)"

setup:
	@echo "make $(ENVIRONMENT);"
	@echo "source $(ENVIRONMENT)bin/activate;"
	@echo "pip install django-debug-toolbar django-extensions;"
	@echo "pip install jedi rope flake8 importmagic yapf ipython==4.2.1;"

up:
	@echo "source _env/bin/activate"

down:
	@echo "source _env/bin/deactivate"


help:
	@echo "To setup python environment, please use 'eval \$$(make setup)'."
	@echo "To start python environment, please use 'eval \$$(make up)'."
	@echo "To deactivate python environment, please use 'eval \$$(make deactivate)'."
