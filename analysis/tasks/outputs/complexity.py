import radon.complexity as rdc

def calculate_code_complexity(total_files_affected, total_files_changed, total_lines_added_in_commit, total_lines_deleted_in_commit, has_bug_fixing):
    # calculate the McCabe's complexity metric
    complexity = 0
    if total_files_changed > 0 and total_lines_added_in_commit > 0:
        complexity = rdc.cc_visit(".", ignore="venv", multi=True)
    
    # adjust the complexity metric if the commit includes bug fixing
    if has_bug_fixing:
        complexity *= 2
    
    # calculate the code complexity score
    code_complexity_score = 5.0 * complexity / 100.0
    
    # round the score to 1 decimal place
    code_complexity_score = round(code_complexity_score, 1)
    
    # return the code complexity score
    return code_complexity_score

# # example usage
# total_files_affected = 10
# total_files_changed = 5
# total_lines_added_in_commit = 100
# total_lines_deleted_in_commit = 50
# has_bug_fixing = True

# code_complexity_score = calculate_code_complexity(total_files_affected, total_files_changed, total_lines_added_in_commit, total_lines_deleted_in_commit, has_bug_fixing)

# print("Code complexity score:", code_complexity_score)


# github (https://github.com/rubik/radon) 
# 1. rubik/radon: Various code metrics for Python code
# Radon is a Python tool that computes various metrics from the source code. Radon can compute:
# McCabe's complexity, i.e. cyclomatic complexity; raw metrics ( ...

# stribny (https://stribny.name/blog/2019/05/measuring-python-code-complexity-with-wily/)
# 2. Measuring Python code complexity with wily
# There is a project called wily based on Halstead complexity measures that we can use to measure 
# complexity in Python projects. There was a talk ...

# stackoverflow (https://stackoverflow.com/questions/72248841/calculate-cyclomatic-complexity-from-file-in-different-programming-language-via)
# 3. Calculate cyclomatic complexity from file in different ...
# The easiest method is probably to call and parse the output of Metrics.exe . If you don't provide
# /out , it will print to stdout, ...

# towardsdatascience (https://towardsdatascience.com/simplify-your-python-code-automating-code-complexity-analysis-with-wily-5c1e90c9a485?gi=51449b2406d1)
# 4. Simplify your Python Code: Automating Code Complexity ...
# Developed by Thomas McCabe in 1976, the metric is calculated from a function's control flow graph, 
# which consists of nodes and edges. Nodes and ...

# realpython (https://realpython.com/python-refactoring/)
# 5. Refactoring Python Applications for Simplicity
# Lines of Code; Maintainability Index; Cyclomatic Complexity. Those are the 3 default metrics in wily. 
# To see those metrics for a specific file (such as ...