import os
from analysis.developers.developers_experience.devs_experience import generate_csv_devs_experience_the_years
import pytest
from analysis.tasks.task_analysis import analyze_tasks
from tests import get_csv_from_json, get_json_object
from utils.file_utils import read_csv_file


def test_analyze_messages(tmp_path, get_csv_from_json, get_json_object):
    # Call the function being tested
    output_file = os.path.abspath('data/useable/json_output.csv')

    # output file name
    output_exp_file = os.path.abspath('data/useable/csv_devs_exp_output.csv')
    generate_csv_devs_experience_the_years(
        get_csv_from_json, get_json_object, output_exp_file)

    # read the generated CSV file
    with open(output_exp_file, 'r') as f:
        rows = [row.strip().split(',') for row in f]

    # assert header row is correct
    assert rows[0] == ['id', '2014', '2016', '2019']

    # assert data rows are correct
    assert rows[1] == ['kaxilnaik@gmail.com', '-1', '0', '1']
    assert rows[2] == ['maximebeauchemin@gmail.com', '0', '-1', '1']
    assert rows[3] == ['noreply@github.com', '-1', '-1', '0']

    result = analyze_tasks(get_json_object, output_file, output_exp_file)
    # Assert the expected number of tasks is found
    assert len(result) == 3

    # Assert the expected tasks are found
    expected_tasks = [
        {
            "id": "",
            "message": "Fix a bug",
            "is_fix_related": False,
            "is_bug_fixing": False,
            "is_refactoring": False,
            "total_lines_added_in_commit": 334,
            "total_lines_deleted_in_commit": 639,
            "total_files_affected": 6,
            "total_files_changed": 2,
            "author_email": "kaxilnaik@gmail.com",
            "committer_email": "noreply@github.com",
            "authored_at": "04/09/2016, 18:46:00",
            "authored_year": "2016",
            "commited_at": "04/09/2019, 18:46:00",
            "commited_year": "2019",
            "commit_time": 4,
            "auther_experience": "0",
            "committer_experience": "0"
        },
        {
            "id": "AIRFLOW-1234",
            "message": "Add a new feature",
            "is_fix_related": True,
            "is_bug_fixing": True,
            "is_refactoring": False,
            "total_lines_added_in_commit": 5023,
            "total_lines_deleted_in_commit": 0,
            "total_files_affected": 52,
            "total_files_changed": 1,
            "author_email": "maximebeauchemin@gmail.com",
            "committer_email": "maximebeauchemin@gmail.com",
            "authored_at": "10/06/2014, 21:29:38",
            "authored_year": "2014",
            "commited_at": "10/06/2014, 21:29:38",
            "commited_year": "2014",
            "commit_time": 4,
            "auther_experience": "0",
            "committer_experience": "0"
        },
        {
            "id": "AIRFLOW-5678",
            "message": "Update documentation",
            "is_fix_related": True,
            "is_bug_fixing": True,
            "is_refactoring": False,
            "total_lines_added_in_commit": 1,
            "total_lines_deleted_in_commit": 1,
            "total_files_affected": 1,
            "total_files_changed": 1,
            "author_email": "maximebeauchemin@gmail.com",
            "committer_email": "kaxilnaik@gmail.com",
            "authored_at": "04/15/2019, 17:40:00",
            "authored_year": "2019",
            "commited_at": "04/15/2019, 17:40:00",
            "commited_year": "2019",
            "commit_time": 3,
            "auther_experience": "1",
            "committer_experience": "1"
        }
    ]

    assert sorted(result, key=lambda x: x['id']) == sorted(
        expected_tasks, key=lambda x: x['id'])

    # Assert the output CSV file was written and contains the expected data

    csv_data = read_csv_file(output_file)
    print(csv_data)

    assert csv_data == [[
        'task_id',
        'task_message',
        'task_type',
        'has_bug_fixing',
        'has_code_refactoring',
        'is_fix_related',
        'is_bug_fixing',
        'is_refactoring',
        'total_lines_added_in_commit',
        'total_lines_deleted_in_commit',
        'total_files_affected',
        'total_files_changed',
        'author_email',
        'committer_email',
        'authored_at',
        'authored_year',
        'commited_at',
        'commited_year',
        'commit_time',
        'auther_experience',
        'committer_experience',
        'code_quality',
        'code_complexity',
        'duration',
    ], [
        'AIRFLOW-1234',
        'Add a new feature',
        '',
        '',
        '',
        'True',
        'True',
        'False',
        '5023',
        '0',
        '52',
        '1',
        'maximebeauchemin@gmail.com',
        'maximebeauchemin@gmail.com',
        '10/06/2014, 21:29:38',
        '2014',
        '10/06/2014, 21:29:38',
        '2014',
        '4',
        '0',
        '0',
        '3.2',
        '1.2',
        '0',
    ], [
        '',
        'Fix a bug',
        '',
        '',
        '',
        'False',
        'False',
        'False',
        '334',
        '639',
        '6',
        '2',
        'kaxilnaik@gmail.com',
        'noreply@github.com',
        '04/09/2016, 18:46:00',
        '2016',
        '04/09/2019, 18:46:00',
        '2019',
        '4',
        '0',
        '0',
        '3.2',
        '1.2',
        '0',
    ], [
        'AIRFLOW-5678',
        'Update documentation',
        '',
        '',
        '',
        'True',
        'True',
        'False',
        '1',
        '1',
        '1',
        '1',
        'maximebeauchemin@gmail.com',
        'kaxilnaik@gmail.com',
        '04/15/2019, 17:40:00',
        '2019',
        '04/15/2019, 17:40:00',
        '2019',
        '3',
        '1',
        '1',
        '3.2',
        '1.2',
        '0',
    ]]

    # Cleanup the output file
    os.remove(output_file)
    os.remove(output_exp_file)
