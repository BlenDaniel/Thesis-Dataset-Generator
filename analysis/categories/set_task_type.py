import os
from analysis.categories.get_task_type import get_task_type
from utils import file_utils, data_utils
import pandas as pd

def set_task_type(output):
    # Load the data from the CSV file
    df = pd.read_csv(output)
    
    # Apply the get_task_type function to the task_message column to generate the task_type column
    df["task_type"] = df["task_message"].apply(get_task_type)

    # Save the updated dataframe to a new CSV file
    output_file = os.path.join(
        os.path.dirname(output), "tasks_type_output.csv")
    df.to_csv(output_file, index=False)
    print(f"There are {len(df)} rows affected.")
