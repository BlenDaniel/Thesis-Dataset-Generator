import csv
from analysis.csv_analysis import analyze_data_devs

from utils.file_utils import read_csv_file
import os

def test_analyze_data(tmp_path):
    # create some test data with 3 columns and 5 rows
    test_data = [
        ['Name', 'Age', 'Gender'],
        ['John', '25', 'Male'],
        ['Jane', '30', 'Female'],
        ['Jack', '25', 'Male'],
        ['Jill', '28', 'Female'],
        ['Jim', '30', 'Male']
    ]
    
    # specify the column index to analyze
    column_indexes = [1, 2]

    # output file name
    output_file = os.path.abspath('data/useable/csv_output.csv')

    # call the analyze_data function
    num_unique_values = analyze_data_devs(test_data, column_indexes, 1, output_file)
    
    # check that the function returns the expected number of unique values
    assert num_unique_values == (3, 2), f"Expected 3, 2 unique values but got {num_unique_values}"
    
    # read in the output CSV file and check that it contains the expected unique values
    csv_data = read_csv_file(output_file)

    # check that each row in the output CSV file is a unique value from the test data
    for row in csv_data[1:]:
        assert row[1] in ['Male', 'Female'], f"Unexpected value '{row[1]}' found in output CSV file"

    # Cleanup the output file
    os.remove(output_file)


