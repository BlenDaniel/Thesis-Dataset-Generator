import csv
import json
import re
import os
from utils.file_utils import read_json_file, save_path


def analyze_messages(json_obj, output):
    # Initialize an empty list to store the tasks
    tasks = []

    # Define the regex pattern to match task IDs and messages
    regex = r"\[([A-Z]+-[0-9]+|[A-Z]+-[A-Z]+)\]\s*(\[(?:[A-Z]+-[0-9]+|[A-Z]+-[A-Z]+)\])?\s*(.*)"

    # Iterate over each commit in the JSON json_obj
    for commit in json_obj["commits"]:
        # Extract the commit message
        message = commit["message"]
        # Use regex to match the task ID and message
        match = re.match(regex, message)
        if match:
            # If the message matches the regex pattern, extract the task ID and message
            task_id = match.group(1)
            if match.group(2):
                task_id += "_" + re.sub(r"[\[\]]", "", match.group(2))
            task_message = match.group(3).strip()
            # Append the task to the list of tasks
            tasks.append({"id": task_id, "message": task_message})

        else:
            # If the message doesn't match the regex pattern, use the entire message as the task message
            task_id = ""
            task_message = message
            # Append the task to the list of tasks
            tasks.append({"id": "", "message": task_message})

    # write out the unique values to the output CSV file
    output_file_name = os.path.basename(output)
    
    # Write the list of tasks to a CSV file
    with open(output, mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(["task_id", "task_message", "task_type"])
        for task in tasks:
            writer.writerow([task["id"], task["message"], ""])

    # Print the number of unique tasks found
    print(f"There are {len(tasks)} unique tasks.")
    return tasks
