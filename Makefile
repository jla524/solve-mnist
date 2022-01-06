#################################################################################
# GLOBALS                                                                       #
#################################################################################
PROJECT_NAME = solve_mnist
PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements:
		poetry install

## Make Dataset
data: requirements
		poetry run $(PYTHON_INTERPRETER) make_dataset.py

## Delete all compiled Python files
clean: 
		find . -type f -name "*.py[co]" -delete
		find . -type d -name "__pycache__" -delete
