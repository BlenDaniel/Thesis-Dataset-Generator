from analysis.developers import devs_analysis
from analysis.developers.developers_experience.devs_experience import generate_csv_devs_authored_the_years, generate_csv_devs_commit_the_years, generate_csv_devs_experience_the_years
from analysis.tasks.categories import set_task_info
from analysis.tasks import task_analysis
from utils import file_utils, data_utils

# Set up the paths to the CSV and JSON files
csv_path = 'data/knox/knox.csv'  # file_utils.choose_file()
json_path = 'data/knox/knox.json'  # file_utils.choose_file()
save_path = file_utils.save_path() + 'knox/'

# Load Json from the path and convert it
json_obj = file_utils.read_json_file(json_path)

# Set up the paths to the tasks CSV and tasks_output
tasks_path = save_path + "tasks.csv"
tasks_output_path = "tasks_output.csv"


# Load csv from the path and convert it to a list of lists
csv_lists = file_utils.read_csv_file(csv_path)


# Step 1
# Analyze the data using the appropriate analysis module
csv_analysis_results = devs_analysis.analyze_data_devs(
    csv_lists, [4, 6], 2, save_path+"developers.csv")

# Step 2
generate_csv_devs_authored_the_years(
    csv_lists, json_obj, save_path + "dev_author_experience.csv")

# Step 3
generate_csv_devs_commit_the_years(
    csv_lists, json_obj, save_path + "dev_commit_experience.csv")

# Step 4
generate_csv_devs_experience_the_years(
    csv_lists, json_obj, save_path + "dev_experience.csv")


# Step 5
# Analyze the data using the appropriate analysis module
json_analysis_results = task_analysis.analyze_tasks(
    json_obj, tasks_path, save_path + 'dev_experience.csv')


# Step 6
set_task_info.set_task_info(tasks_path, tasks_output_path)
