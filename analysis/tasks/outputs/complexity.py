
def calculate_task_complexity(total_files_affected, total_files_changed, total_lines_added_in_commit,
                              total_lines_deleted_in_commit, has_bug_fixing):
    """
    Calculates the task complexity based on the number of files affected, files changed,
    lines added, lines deleted in a commit, and whether the commit includes a bug fixing.
    The higher the number of affected files, files changed, and lines added/deleted,
    the higher the task complexity. Also, a commit with a bug fixing is considered more complex.
    Returns a float between 1 and 5, where 5 represents the highest task complexity.
    """

    task_file_complexity = get_file_complexity_rating(
        total_files_affected, total_files_changed)
    task_lines_complexity = get_lines_complexity_rating(
        total_lines_added_in_commit, total_lines_deleted_in_commit)

    # calculate overall task complexity based on the complexity ratings and bug fixing
    task_complexity = task_file_complexity + task_lines_complexity

    if has_bug_fixing:
        task_complexity *= 1.2
    return min((5 * task_complexity) / 10, 5.0)


def get_file_complexity_rating(total_files_affected, total_files_changed):
    # Minimal: 0-2 files affected or changed
    if total_files_affected + total_files_changed <= 10:
        return 1
    # Low: 3-5 files affected or changed
    elif total_files_affected + total_files_changed <= 20:
        return 2
    # Moderate: 6-9 files affected or changed
    elif total_files_affected + total_files_changed <= 50:
        return 3
    # High: 10-15 files affected or changed
    elif total_files_affected + total_files_changed <= 100:
        return 4
    # Very High: 16+ files affected or changed
    else:
        return 5


def get_lines_complexity_rating(total_lines_added_in_commit, total_lines_deleted_in_commit):
    # Minimal: 0-10 lines added or deleted
    if total_lines_added_in_commit + total_lines_deleted_in_commit <= 50:
        return 1
    # Low: 11-50 lines added or deleted
    elif total_lines_added_in_commit + total_lines_deleted_in_commit <= 100:
        return 2
    # Moderate: 51-200 lines added or deleted
    elif total_lines_added_in_commit + total_lines_deleted_in_commit <= 200:
        return 3
    # High: 201-500 lines added or deleted
    elif total_lines_added_in_commit + total_lines_deleted_in_commit <= 500:
        return 4
    # Very High: 501+ lines added or deleted
    else:
        return 5
