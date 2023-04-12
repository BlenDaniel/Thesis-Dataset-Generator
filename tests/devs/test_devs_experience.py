import os
from analysis.developers.developers_experience.devs_experience import generate_csv_devs_authored_the_years, generate_csv_devs_commit_the_years, generate_csv_devs_experience_the_years, get_list_of_years, get_year_from_date
import pytest
from tests import get_csv_from_json, get_json_object
from utils.file_utils import read_csv_file



def test_generate_csv_devs_experience_the_years(get_csv_from_json, get_json_object):
    # output file name
    output_file = os.path.abspath('data/useable/csv_devs_exp_output.csv')
    generate_csv_devs_experience_the_years(get_csv_from_json, get_json_object, output_file)

    # read the generated CSV file
    with open(output_file, 'r') as f:
        rows = [row.strip().split(',') for row in f]

    # assert header row is correct
    assert rows[0] == ['id', '2014', '2016', '2019']

    # assert data rows are correct
    assert rows[1] == ['kaxilnaik@gmail.com', '-1', '0', '1']
    assert rows[2] == ['maximebeauchemin@gmail.com', '0', '-1', '1']
    assert rows[3] == ['noreply@github.com', '-1', '-1', '0']
    # Cleanup the output file
    os.remove(output_file)


def test_generate_csv_devs_authored_the_years(get_csv_from_json, get_json_object):
    # output file name
    output_file = os.path.abspath('data/useable/csv_devs_author_output.csv')
    generate_csv_devs_authored_the_years(get_csv_from_json, get_json_object, output_file)
    
    # read the generated CSV file
    with open(output_file, 'r') as f:
        rows = [row.strip().split(',') for row in f]


    assert rows[0] == ['id', '2014', '2016', '2019', 'total_authored']
    assert rows[1] == ['kaxilnaik@gmail.com', '0', '1', '0', '1']
    assert rows[2] == ['maximebeauchemin@gmail.com', '1', '0', '1', '2']

    # Cleanup the output file
    os.remove(output_file)

def test_generate_csv_devs_commit_the_years(get_csv_from_json, get_json_object):
    # output file name
    output_file = os.path.abspath('data/useable/csv_devs_commit_output.csv')
    generate_csv_devs_commit_the_years(get_csv_from_json, get_json_object, output_file)
    rows = read_csv_file(output_file)
    assert rows[0] == ['id', '2014', '2016', '2019', 'total_commits']
    print(rows[1], rows[2], rows[3])
    assert rows[1] == ['kaxilnaik@gmail.com', '0', '0', '1', '1']
    assert rows[2] == ['maximebeauchemin@gmail.com', '1', '0', '0', '1']
    assert rows[3] == ['noreply@github.com', '0', '0', '1', '1']

    # Cleanup the output file
    os.remove(output_file)

def test_get_list_of_years():
    input_list = [
            ['id', 'branch', 'message', 'parent_ids', 'author', 'authored_at', 'committer', 'committed_at'],
            ['1', 'master', 'initial commit', '', 'user1', '04/15/2019, 17:40:00', 'user1', '04/15/2019, 17:40:00'],
            ['2', 'feature1', 'add feature1', '1', 'user2', '04/16/2019, 09:30:00', 'user1', '04/17/2019, 14:20:00'],
            ['3', 'feature2', 'add feature2', '2', 'user3', '05/01/2020, 11:45:00', 'user2', '05/02/2019, 13:10:00'],
            ['4', 'master', 'fix bug', '1', 'user1', '06/10/2021, 19:30:00', 'user2', '06/11/2019, 10:15:00']
        ]
    
    expected_output = [2019, 2020, 2021]
    assert get_list_of_years(input_list) == expected_output


def test_get_year_from_date():
    date_string = '04/15/2019, 17:40:00'
    expected_output = 2019
    assert get_year_from_date(date_string) == expected_output
