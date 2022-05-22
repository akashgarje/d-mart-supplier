import pytest
from beginner_task import CsvToJson


@pytest.fixture()
def instance():
    csvtojson = CsvToJson()
    return csvtojson


def test_Extension(instance):
    csv_file = instance.data_file
    instance.main(csv_file=csv_file)
    if csv_file.lower().endswith('.csv'):
        print("Successful")
    else:
        raise Exception("File Provided is not CSV")


def test_function(instance):
    csv_file = instance.data_file
    try:
        instance.main(csv_file=csv_file)
    except NameError:
        print("CsvToJson Not Defined")
    else:
        print("Successful!")
    # data = 'data.csv'
    # assert CsvToJson.main(data) == instance.main(data), "Error"


