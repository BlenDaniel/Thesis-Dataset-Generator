import csv
import re
import os
from analysis.tasks.categories.get_task_info import get_has_bug_fixing, get_has_refactoring
from analysis.tasks.outputs.quality import calculate_code_quality
from analysis.tasks.outputs.complexity import calculate_task_complexity
from analysis.tasks.outputs.duration import calculate_duration

from utils.file_utils import read_csv_file
from utils.time_utils import categorize_time, get_year


def analyze_tasks(json_obj, output, experience_path):
    # Initialize an empty list to store the tasks
    tasks = []

    # Define the regex pattern to match task IDs and messages
    regex = r"\[([A-Z]+-[0-9]+|[A-Z]+-[A-Z]+)\]\s*(\[(?:[A-Z]+-[0-9]+|[A-Z]+-[A-Z]+)\])?\s*(.*)"

    # Open experience csv
    experience_reader = read_csv_file(experience_path)

    # List of the header row (id, 20XX....)
    header = experience_reader[0]
    print('Timeline of the project: ', header[1:])

    # Iterate over each commit in the JSON json_obj
    for commit in json_obj["commits"]:
        # Extract the author and committer
        authored_by = commit["authored_by"]["author_email"]
        committed_by = commit["committed_by"]["committer_email"]

        # Extract time information
        authored_at = commit["authored_at"]
        authored_year = get_year(authored_at)
        commited_at = commit["commited_at"]
        commited_year = get_year(commited_at)

        # Commit info
        commit_time = categorize_time(commited_at)

        # Wanted year
        a_year_index = header.index(authored_year)
        c_year_index = header.index(commited_year)

        # Experience in the company
        auther_experience = 0
        for row in experience_reader[1:]:
            if (row[0] == commit["authored_by"]["author_email"]):
                auther_experience = row[a_year_index]

        committer_experience = 0
        for row in experience_reader[1:]:
            if (row[0] == commit["committed_by"]["committer_email"]):
                committer_experience = row[c_year_index]

        # Extract the commit is_fix_related
        is_fix = commit["is_fix_related"]
        # Extract the commit is_bug_fixing
        is_bug = commit["is_bug_fixing"]
        # Extract the commit is_refactoring
        is_ref = commit["is_refactoring"]
        # Extract the commit total lines added in task
        added_lines = commit["total_lines_added_in_commit"]
        # Extract the commit total lines deleted in commit
        deleted_lines = commit["total_lines_deleted_in_commit"]
        # Extract the commit total files changed
        files_affected = commit["files_changed_total"]
        # Extract the commit total files changed
        files_changed = len(commit["changes"])
        # Extract the commit message
        message = commit["message"]

        # total code addition/deletions
        total_file_additions = 0
        total_file_deletions = 0

        for change in commit["changes"]:
            total_file_additions += change["file_additions"]
            total_file_deletions += change["file_deletions"]

        # Duration, code quality and code complexity is the focus here
        duration = calculate_duration(authored_at, commited_at)
        has_refactoring = get_has_refactoring(
            commit["message"], commit['is_refactoring'])
        code_quality = calculate_code_quality(
            files_affected, files_changed, added_lines, deleted_lines, total_file_additions, total_file_deletions, has_refactoring)
        has_bug_fixing = get_has_bug_fixing(
            commit["message"], commit['is_bug_fixing'] or commit['is_fix_related'])
        code_complexity = calculate_task_complexity(files_affected, files_changed, added_lines,
                                                    deleted_lines, has_bug_fixing)

        # Use regex to match the task ID and message
        match = re.match(regex, message)
        if match:
            # If the message matches the regex pattern, extract the task ID and message
            task_id = match.group(1)
            if match.group(2):
                task_id += "_" + re.sub(r"[\[\]]", "", match.group(2))
            task_message = match.group(3).strip()
            # Append the task to the list of tasks
            tasks.append({"id": task_id,
                          "message": task_message,
                          "is_fix_related": is_fix,
                          "is_bug_fixing": is_bug,
                          "is_refactoring": is_ref,
                          "total_lines_added_in_commit": added_lines,
                          "total_lines_deleted_in_commit": deleted_lines,
                          "total_files_affected": files_affected,
                          "total_files_changed": files_changed,
                          "author_email": authored_by,
                          "committer_email": committed_by,
                          "authored_at": authored_at,
                          "authored_year": authored_year,
                          "commited_at": commited_at,
                          "commited_year": commited_year,
                          "commit_time": commit_time,
                          "auther_experience": auther_experience,
                          "committer_experience": committer_experience,
                          "code_quality": code_quality,
                          "code_complexity": code_complexity,
                          "duration": duration,
                          })

        else:
            # If the message doesn't match the regex pattern, use the entire message as the task message
            task_id = ""
            task_message = message
            # Append the task to the list of tasks
            tasks.append({"id": "",
                          "message": task_message,
                          "is_fix_related": is_fix,
                          "is_bug_fixing": is_bug,
                          "is_refactoring": is_ref,
                          "total_lines_added_in_commit": added_lines,
                          "total_lines_deleted_in_commit": deleted_lines,
                          "total_files_affected": files_affected,
                          "total_files_changed": files_changed,
                          "author_email": authored_by,
                          "committer_email": committed_by,
                          "authored_at": authored_at,
                          "authored_year": authored_year,
                          "commited_at": commited_at,
                          "commited_year": commited_year,
                          "commit_time": commit_time,
                          "auther_experience": auther_experience,
                          "committer_experience": committer_experience,
                          "code_quality": code_quality,
                          "code_complexity": code_complexity,
                          "duration": duration,
                          })

    # write out the unique values to the output CSV file
    output_file_name = os.path.basename(output)

    # Write the list of tasks to a CSV file
    with open(output, mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(["task_id",
                         "task_message",
                         "task_type",
                         "has_bug_fixing",
                         "has_code_refactoring",
                         'is_fix_related',
                         'is_bug_fixing',
                         'is_refactoring',
                         'total_lines_added_in_commit',
                         'total_lines_deleted_in_commit',
                         'total_files_affected',
                         'total_files_changed',
                         "author_email",
                         "committer_email",
                         "authored_at",
                         "authored_year",
                         "commited_at",
                         "commited_year",
                         "commit_time",
                         "auther_experience",
                         "committer_experience",
                         "code_quality",
                         "code_complexity",
                         "communication",
                         ])

        for task in tasks:
            writer.writerow([task["id"],
                             task["message"],
                             "",
                             "",
                             "",
                             task['is_fix_related'],
                             task['is_bug_fixing'],
                             task['is_refactoring'],
                             task['total_lines_added_in_commit'],
                             task['total_lines_deleted_in_commit'],
                             task['total_files_affected'],
                             task['total_files_changed'],
                             task["author_email"],
                             task["committer_email"],
                             task["authored_at"],
                             task["authored_year"],
                             task["commited_at"],
                             task["commited_year"],
                             task["commit_time"],
                             task["auther_experience"],
                             task["committer_experience"],
                             task["code_quality"],
                             task["code_complexity"],
                             task["duration"],
                             ])

    # Print the number of unique tasks found
    print(f"There are {len(tasks)} unique tasks.")
    return tasks
