# Project Install Instructions

## Install

1. git clone https://github.com/Monica-Mathew/is601homework3-spring2025.git

## Activate virtual environment

1. source venv/bin/activate
2. pip3 install -r requirements.txt
3. pip3 freeze > requirements.txt 
4. python3 main.py 2 2 add (To run main.py)
4. deactivate


## Testing
1. pytest
2. pytest --pylint 
3. pytest --pylint --cov
4. pytest --num_records=100
5. pytest --cov=. --cov-report=html (To see the coverage report line by line)
