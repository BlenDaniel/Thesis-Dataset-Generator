import os
from analysis.tasks.categories.get_task_info import get_task_info
import pandas as pd

def set_task_info(output, new_output):
    # Load the data from the CSV file
    df = pd.read_csv(output)
    
    # Apply the get_task_type function to the task_message column to generate the task_type column
    df[["task_type", "has_bug_fixing", "has_code_refactoring"]] = df["task_message"].apply(lambda x: pd.Series(get_task_info(x)))


    # Save the updated dataframe to a new CSV file
    output_file = os.path.join(
        os.path.dirname(output), new_output)
    df.to_csv(output_file, index=False)
    print(f"There are {len(df)} rows affected.")
