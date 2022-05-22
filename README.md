
## Technology Choices:

I have used Python-pandas as the technology, since Python comes with many built-in functionalities and libraries. I have used pandas from Python
since reading a CSV data, grouping particular columns' data helps to create nested structure. I have created application using PyCharm IDE since
PyCharm provides very efficient debugging. Evaluating particular expression can be achieved using PyCharm debugger. Also for unit tests, I have
used Pytest which is built-in unit testing tool of Python.

Please find dynamic_code.txt where I tried to make the application dynamic (provided csv data may vary in size thus created function) using 
recursion but there I was getting errors. 

## Instructions to run solution:

For running the TestDmart.py I have used terminal with the command "pytest -v TestDmart.py".
If data provided is CSV and CsvToJson is imported in TestDmart.py, tests pass.
If data_file extension is changed, test_Extension test fails.
Also if CsvToJson is not imported, test_Function fails. 

## Link to git repository:

Please find the github repository: https://github.com/akashgarje/d-mart-supplier