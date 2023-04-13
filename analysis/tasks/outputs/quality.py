def calculate_code_quality(total_files_affected, total_files_changed, total_lines_added_in_commit, total_lines_deleted_in_commit, file_additions, file_deletions, has_refactoring):
    # calculate the total number of lines changed in the commit
    total_lines_changed = total_lines_added_in_commit + total_lines_deleted_in_commit
    
    # calculate the CCP metric
    ccp = 0
    if total_files_changed > 0 and total_lines_changed > 0:
        ccp = total_files_affected / (total_files_changed * total_lines_changed)
    
    # adjust the CCP metric if the commit includes refactoring
    if has_refactoring:
        ccp *= 2
    
    # calculate the percentage of lines added to the total number of lines changed
    lines_added_percentage = 0
    if total_lines_added_in_commit + total_lines_deleted_in_commit > 0:
        lines_added_percentage = total_lines_added_in_commit / (total_lines_added_in_commit + total_lines_deleted_in_commit)
    
    # calculate the code quality score
    code_quality_score = 5.0 * (ccp + lines_added_percentage) / 2.0
    
    # round the score to 1 decimal place
    code_quality_score = round(code_quality_score, 1)
    
    # return the code quality score
    return code_quality_score


# Sources

# arxiv (https://arxiv.org/pdf/2007.10912.pdf)
# 1. The Corrective Commit Probability Code Quality Metric
# Abstract—We present a code quality metric, Corrective Commit Proba- bility (CCP), 
# measuring the probability that a commit reflects corrective ...

# arxiv (https://arxiv.org/pdf/2007.10912.pdf)
# 2. The Corrective Commit Probability Code Quality Metric
# We present a code quality metric, Corrective Commit Probability (CCP), measuring the 
# probability that a commit reflects corrective maintenance.

# semanticscholar (https://www.semanticscholar.org/paper/The-Corrective-Commit-Probability-Code-Quality-Amit-Feitelson/1613bad06e6540f93d69100ee477628950f1799d)
# 3. [PDF] The Corrective Commit Probability Code Quality Metric
# We present a code quality metric, Corrective Commit Probability (CCP), measuring 
# the probability that a commit reflects corrective ...

# Realpython (https://realpython.com/python-code-quality/)
# 4. Python Code Quality: Tools & Best Practices
# In this article, we'll identify high-quality Python code and show you how to improve the quality 
# of your own code. We'll analyze and compare tools you can ...

# igor (https://www.igor.pro.br/publica/papers/EMSE2020.pdf)
# 5. Code and Commit Metrics of Developer Productivity
# Based on commit information, we calculated the productivity of each developer by applying each 
# commit-based metrics to their commits in the ...