import io
import os
from analysis.tasks.categories.get_task_info import get_task_info
from analysis.tasks.categories.set_task_info import set_task_info
from utils.file_utils import read_csv_file
import pandas as pd


def test_task_type():
    # Create a sample CSV file
    test_data = [
        ["task_id", "task_message", "task_type",
            "has_bug_fixing", "has_code_refactoring"],
        ["AIRFLOW-1234", "Add a new feature", "",  "",  ""],
        ["AIRFLOW-5678", "Update documentation", "",  "",  ""],
        ["AIRFLOW-9012", "Fix a bug", "",  "",  ""],
    ]

    # Output file name
    output_file = os.path.abspath('data/useable/test_task_type_output.csv')

    # Convert test_data to a pandas DataFrame
    df = pd.DataFrame(test_data[1:], columns=test_data[0])

    output = 'data/useable/test_data.csv'

    # Save the DataFrame to a CSV file
    df.to_csv(output, index=False)

    set_task_info(output, output_file)

    # Load the data from the updated CSV file
    data = read_csv_file(output_file)

    # Assert that each task has a valid task type
    for row in data[1:]:
        assert row[2] in ["Feature requests or new feature", "Bug fixes",
                          "Code Refactoring", "Documentation", "Testing", "Deployment", "Maintenance"]

    # Cleanup the output file
    os.remove(output)
    os.remove(output_file)
