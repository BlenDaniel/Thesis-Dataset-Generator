import os
from analysis.categories.get_task_type import get_task_type
from utils.file_utils import read_csv_file
import pandas as pd


def test_task_type():
    # Create a sample CSV file
    test_data = [
        ["task_id", "task_message", "task_type"],
        ["AIRFLOW-1234", "Add a new feature", ""],
        ["AIRFLOW-5678", "Update documentation", ""],
        ["AIRFLOW-9012", "Fix a bug", ""],
    ]

    # Output file name
    output_file = os.path.abspath('data/useable/test_task_type_output.csv')

    # Convert test data to DataFrame
    df = pd.DataFrame(test_data[1:], columns=test_data[0])

    # Apply the get_task_type function to the task_message column to generate the task_type column
    df["task_type"] = df["task_message"].apply(get_task_type)

    # Save the updated dataframe to a new CSV file
    df.to_csv(output_file, index=False)

    # Load the data from the updated CSV file
    data = read_csv_file(output_file)

    # Assert that each task has a valid task type
    for row in data[1:]:
        assert row[2] in ["Feature requests or new feature", "Bug fixes", "Code Refactoring", "Documentation", "Testing", "Deployment", "Maintenance"]

    # Cleanup the output file
    os.remove(output_file)

