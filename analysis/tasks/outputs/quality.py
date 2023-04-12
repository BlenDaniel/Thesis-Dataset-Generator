
def calculate_code_quality(total_files_affected, total_files_changed, total_lines_added_in_commit, 
                           total_lines_deleted_in_commit, file_additions, file_deletions, has_refactoring):
    """
    Calculates the code quality score based on the number of files affected, the number of files changed, the total 
    lines added in the commit, the total lines deleted in the commit, the number of file additions and the number of 
    file deletions, and whether the commit includes code refactoring.
    
    Returns a score between 0.0 and 5.0, rounded to 1 decimal place.
    """
    if total_files_affected == 0 or total_files_changed == 0:
        return 0.0

    # calculate the percentage of lines added to the total number of lines changed
    lines_added_percentage = total_lines_added_in_commit / (total_lines_added_in_commit + total_lines_deleted_in_commit)

    # calculate the percentage of files added to the total number of files changed
    files_added_percentage = file_additions / (file_additions + file_deletions)

    # calculate the score based on the percentage of lines added, files added, and whether refactoring occurred
    if has_refactoring:
        score = (lines_added_percentage * 0.5 + files_added_percentage * 0.3 + 0.2) * 5.0
    else:
        score = (lines_added_percentage * 0.7 + files_added_percentage * 0.3) * 5.0

    return round(score, 1)
