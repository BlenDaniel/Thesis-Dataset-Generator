import os
import pytest
from analysis.json_analysis import analyze_messages
from utils.file_utils import read_csv_file


@pytest.fixture
def test_data():
    data = {
        "project_name": "apache/airflow",
        "commits": [
            {
                "commit_id": "1047940ca4363b04044c4963b9c88f7632746407",
                "commit_branch": "master",
                "message": "[AIRFLOW-1234] Add a new feature",
            },
            {
                "commit_id": "7b041134a222e1fb2bc3429d9a7fca90327e7890",
                "commit_branch": "dev",
                "message": "Fix a bug",
            },
            {
                "commit_id": "be3cc3bc94d4960ce34389b2a25eae18aa5f8a31",
                "commit_branch": "master",
                "message": "[AIRFLOW-5678] Update documentation",
            },
        ]
    }
    return data



def test_analyze_messages(tmp_path, test_data):
    # Call the function being tested
    output_file = os.path.abspath('data/useable/json_output.csv')

    result = analyze_messages(test_data, output_file)
    # Assert the expected number of tasks is found
    assert len(result) == 3

    # Assert the expected tasks are found
    expected_tasks = [
        {"id": "AIRFLOW-1234", "message": "Add a new feature"},
        {'id': '', 'message': 'Fix a bug'},
        {"id": "AIRFLOW-5678", "message": "Update documentation"},
    ]
    assert all(expected_task in result for expected_task in expected_tasks)

    # Assert the output CSV file was written and contains the expected data
  

    csv_data = read_csv_file(output_file)

    assert csv_data == [
        ["task_id", "task_message", "task_type"],
        ['AIRFLOW-1234', 'Add a new feature', ''],
        ['', 'Fix a bug', ''],
        ['AIRFLOW-5678', 'Update documentation', ''],
    ]

    # Cleanup the output file
    os.remove(output_file)
