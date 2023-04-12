from analysis.developers import devs_analysis
from analysis.developers.developers_experience.devs_experience import generate_csv_devs_authored_the_years, generate_csv_devs_commit_the_years, generate_csv_devs_experience_the_years
from analysis.tasks.categories import set_task_info
from analysis.tasks import task_analysis
from utils import file_utils, data_utils

# # Set up the paths to the CSV and JSON files
# csv_path = file_utils.choose_file()


# # Load csv from the path and convert it to a list of lists
# csv_lists = file_utils.read_csv_file(csv_path)

# # Analyze the data using the appropriate analysis module
# csv_analysis_results = csv_analysis.analyze_data_devs(csv_lists, [4, 6], 2, file_utils.save_path() +"developers.csv")
# print(csv_analysis_results)



# generate_csv_devs_authored_the_years("data/airflow.csv", "data/airflow.json", "data/useable/dev_author_experience.csv")
# generate_csv_devs_commit_the_years("data/airflow.csv", "data/airflow.json", "data/useable/dev_commit_experience.csv")
# generate_csv_devs_experience_the_years("data/airflow.csv", "data/airflow.json", "data/useable/dev_experience.csv")

# # Set up the paths to the CSV and JSON files
# json_path = file_utils.choose_file()

# # Load Json from the path and convert it
# json_obj = file_utils.read_json_file("data/airflow.json")

# # Analyze the data using the appropriate analysis module
# json_analysis_results = task_analysis.analyze_tasks(
#     json_obj, file_utils.save_path() + "tasks.csv", 'data/useable/dev_experience.csv')

# Set up the paths to the CSV and JSON files
csv_tasks_path = file_utils.choose_file()
set_task_info.set_task_info(csv_tasks_path)


