from analysis import csv_analysis, json_analysis
from analysis.categories import set_task_type
from utils import file_utils, data_utils

# # Set up the paths to the CSV and JSON files
# csv_path = file_utils.choose_file()

# # Load csv from the path and convert it to a list of lists
# csv_lists = file_utils.read_csv_file(csv_path)

# # Analyze the data using the appropriate analysis module
# csv_analysis_results = csv_analysis.analyze_data_devs(csv_lists, [4, 6], 2, file_utils.save_path() +"developers.csv")
# print(csv_analysis_results)


# # Set up the paths to the CSV and JSON files
# json_path = file_utils.choose_file()

# # Load Json from the path and convert it 
# json_obj = file_utils.read_json_file(json_path)

# # Analyze the data using the appropriate analysis module
# json_analysis_results = json_analysis.analyze_messages(json_obj,file_utils.save_path() + "tasks.csv")

# Set up the paths to the CSV and JSON files
# csv_tasks_path = file_utils.choose_file()
# set_task_type.set_task_type(csv_tasks_path)