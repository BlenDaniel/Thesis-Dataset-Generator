import pytest
import json


test_data_json = {
    "project_name": "apache/airflow",
    "commits": [
        {
            "commit_id": "1047940ca4363b04044c4963b9c88f7632746407",
            "commit_branch": "master",
            "message": "[AIRFLOW-1234] Add a new feature",
            "parent_ids": [

            ],
            "total_lines_added_in_commit":5023,
            "total_lines_deleted_in_commit":0,
            "authored_at":"10/06/2014, 21:29:38",
            "authored_by":{
                "author_username": "mistercrunch",
                "author_id": "MDQ6VXNlcjQ4NzQzMw==",
                "author_email": "maximebeauchemin@gmail.com",
                "author_name": "Maxime Beauchemin"
            },
            "commited_at": "10/06/2014, 21:29:38",
            "committed_by": {
                "committer_username": "mistercrunch",
                "committer_id": "MDQ6VXNlcjQ4NzQzMw==",
                "committer_email": "maximebeauchemin@gmail.com",
                "committer_name": "Maxime Beauchemin"
            },
            "files_changed_total": 52,
            "is_bug_linked": False,
            "is_fix_related": True,
            "is_bug_fixing": True,
            "is_refactoring": False,
            "changes": [
                {
                    "file_path": "airflow/contrib/example_dags/example_gcs_to_gdrive.py",
                    "previous_file_path": "airflow/contrib/example_dags/example_gcs_to_gdrive.py",
                    "file_additions": 59,
                    "file_deletions": 0,
                    "file_id": "87ca7b21-9fc8-11ec-95f7-482ae32cf5b4"
                }
            ]
        },
        {
            "commit_id": "7b041134a222e1fb2bc3429d9a7fca90327e7890",
            "commit_branch": "dev",
            "message": "Fix a bug",
            "parent_ids": [
                "da1be99178cccad7510ed637aee2da2d30b4ceb9"
            ],
            "total_lines_added_in_commit":334,
            "total_lines_deleted_in_commit":639,
            "authored_at":"04/09/2016, 18:46:00",
            "authored_by":{
                "author_username": "kaxil",
                "author_id": "MDQ6VXNlcjg4MTE1NTg=",
                "author_email": "kaxilnaik@gmail.com",
                "author_name": "Kaxil Naik"
            },
            "commited_at": "04/09/2019, 18:46:00",
            "committed_by": {
                "committer_username": None,
                "committer_id": None,
                "committer_email": "noreply@github.com",
                "committer_name": "GitHub"
            },
            "files_changed_total": 6,
            "is_bug_linked": False,
            "is_fix_related": False,
            "is_bug_fixing": False,
            "is_refactoring": False,
            "changes": [
                {
                    "file_path": "airflow/contrib/hooks/gdrive_hook.py",
                    "previous_file_path": "airflow/contrib/hooks/gdrive_hook.py",
                    "file_additions": 135,
                    "file_deletions": 0,
                    "file_id": "87ca7b22-9fc8-11ec-b42b-482ae32cf5b4"
                },
                {
                    "file_path": "airflow/contrib/operators/gcs_to_gdrive_operator.py",
                    "previous_file_path": "airflow/contrib/operators/gcs_to_gdrive_operator.py",
                    "file_additions": 147,
                    "file_deletions": 0,
                    "file_id": "87ca7b23-9fc8-11ec-a3b2-482ae32cf5b4"
                }
            ]
        },
        {
            "commit_id": "be3cc3bc94d4960ce34389b2a25eae18aa5f8a31",
            "commit_branch": "master",
            "message": "[AIRFLOW-5678] Update documentation",
            "parent_ids": [
                "1d06a322d641c5709c0cf431a5e769050adcca5b"
            ],
            "total_lines_added_in_commit":1,
            "total_lines_deleted_in_commit":1,
            "authored_at":"04/15/2019, 17:40:00",
            "authored_by":{
                "author_username": "mistercrunch",
                "author_id": "MDQ6VXNlcjQ4NzQzMw==",
                "author_email": "maximebeauchemin@gmail.com",
                "author_name": "Maxime Beauchemin"
            },
            "commited_at": "04/15/2019, 17:40:00",
            "committed_by": {
                "committer_username": "kaxil",
                "committer_id": "MDQ6VXNlcjg4MTE1NTg=",
                "committer_email": "kaxilnaik@gmail.com",
                "committer_name": "Kaxil Naik"
            },
            "files_changed_total": 1,
            "is_bug_linked": False,
            "is_fix_related": True,
            "is_bug_fixing": True,
            "is_refactoring": False,
            "changes": [
                {
                    "file_path": "docs/howto/operator/gcp/gcs_to_gdrive.rst",
                    "previous_file_path": "docs/howto/operator/gcp/gcs_to_gdrive.rst",
                    "file_additions": 90,
                    "file_deletions": 0,
                    "file_id": "87ca7b24-9fc8-11ec-a487-482ae32cf5b4"
                }
            ]
        }
    ]
}


@pytest.fixture
def get_csv_from_json():

    # Load the JSON data
    data = json.loads(json.dumps(test_data_json))

    # Define the headers
    headers = ['id',
               'branch',
               'message',
               'parent_ids',
               'author',
               'authored_at',
               'committer',
               'committed_at',
               'commit_additions',
               'commit_deletions',
               'changed_files',
               'is_bug_linked',
               'is_fix_related',
               'is_bug_fixing',
               'is_refactoring',
               'file_path',
               'previous_file_path',
               'file_additions',
               'file_deletions',
               'file_id',
               ]

    # Initialize the list of lists with the headers
    list_of_lists = [headers]

    # Extract the relevant fields for each commit and append to the list of lists
    for commit in data['commits']:
        id = commit['commit_id']
        branch = commit['commit_branch']
        message = commit['message']
        parent_ids = commit['parent_ids']
        author = commit['authored_by']['author_username']
        authored_at = commit['authored_at']
        committer = commit['committed_by']['committer_username']
        committed_at = commit['commited_at']
        commit_additions = commit['total_lines_added_in_commit']
        commit_deletions = commit['total_lines_deleted_in_commit']
        changed_files = commit['files_changed_total']
        is_bug_linked = commit['is_bug_linked']
        is_fix_related = commit['is_fix_related']
        is_bug_fixing = commit['is_bug_fixing']
        is_refactoring = commit['is_refactoring']
        file_path = commit['changes'][0]['file_path']
        previous_file_path = commit['changes'][0]['previous_file_path']
        file_additions = commit['changes'][0]['file_additions']
        file_deletions = commit['changes'][0]['file_deletions']
        file_id = commit['changes'][0]['file_id']
        list_of_lists.append([
            id, branch, message, parent_ids, author, authored_at,
            committer, committed_at, commit_additions, commit_deletions,
            changed_files, is_bug_linked, is_fix_related, is_bug_fixing,
            is_refactoring, file_path, previous_file_path, file_additions,
            file_deletions, file_id
        ])

    return list_of_lists


@pytest.fixture
def get_json():
    return test_data_json


@pytest.fixture
def get_json_object():
    return json.loads(json.dumps(test_data_json))
