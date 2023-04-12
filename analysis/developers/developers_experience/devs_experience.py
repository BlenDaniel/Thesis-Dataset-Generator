import datetime
from utils.file_utils import read_csv_file, read_json_file
import csv
from dateutil import parser

def generate_csv_devs_experience_the_years(input_csv_list, json_obj, output):

    with open(output, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # get the list of years from the input CSV file
        list_of_years = get_list_of_years(input_csv_list)

        # write the header row to the output CSV file
        header_row = list(list_of_years)
        header_row.insert(0, 'id')
        csvwriter.writerow(header_row)

        # get the set of unique developers from the input JSON file
        devs = set()
        for commit in json_obj["commits"]:
            if 'authored_by' in commit and 'author_email' in commit['authored_by']:
                dev = commit['authored_by']['author_email']
                devs.add(dev)
            if 'committed_by' in commit and 'committer_email' in commit['committed_by']:
                dev = commit['committed_by']['committer_email']
                devs.add(dev)

        # create a dictionary to store the number of commits made by each developer in each year
        active_by_year_by_dev = {
            dev: {str(year): -1 for year in list_of_years} for dev in devs}
       
        # iterate through the rows of the input JSON file and count the number of commits made by each developer in each year
        for commit in json_obj["commits"]:
            if 'authored_by' in commit and 'author_email' in commit['authored_by']:
                year = get_year_from_date(commit['authored_at'])
                dev = commit['authored_by']['author_email']
                if(active_by_year_by_dev[dev][str(year)] == -1):
                    active_by_year_by_dev[dev][str(year)] = 0
                else:
                    active_by_year_by_dev[dev][str(year)] = 1

            if 'committed_by' in commit and 'committer_email' in commit['committed_by']:
                year = get_year_from_date(commit['commited_at'])
                dev = commit['committed_by']['committer_email']
                if(active_by_year_by_dev[dev][str(year)] == -1):
                    active_by_year_by_dev[dev][str(year)] = 0
                else:
                    active_by_year_by_dev[dev][str(year)] = 1

        # calculate the years of experience for each developer
        for dev in devs:
            counter = 0
            for year in list_of_years:
                if active_by_year_by_dev[dev][str(year)] > -1:
                    active_by_year_by_dev[dev][str(year)] = counter
                    counter += 1

        # write out the data rows to the output CSV file
        for dev in sorted(devs):
            data_row = [dev]
            for year in list_of_years:
                data_row.append(active_by_year_by_dev[dev][str(year)])
            csvwriter.writerow(data_row)
        print(f"The list of unique values has been written to {len(list(devs))}.")
    

def generate_csv_devs_authored_the_years(input_csv_list, json_obj, output):
    # write out the unique values to the output CSV file
    with open(output, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        list_of_years = get_list_of_years(input_csv_list)
        # write the header row
        header_row = list(list_of_years)
        header_row.insert(0, 'id')
        header_row.append('total_authored')
        csvwriter.writerow(header_row)

        # get the set of unique developers
        devs = set()
        for commit in json_obj["commits"]:
            if 'authored_by' in commit and 'author_email' in commit['authored_by']:
                dev = commit['authored_by']['author_email']
                devs.add(dev)

        # create a dictionary to store the number of commits made by each developer in each year
        authors_by_year_by_dev = {
            dev: {str(year): 0 for year in list_of_years} for dev in devs}

        # iterate through the rows of the CSV file and count the number of commits made by each developer in each year
        for commit in json_obj["commits"]:
            if 'authored_by' in commit and 'author_email' in commit['authored_by']:
                year = get_year_from_date(commit['authored_at'])
                dev = commit['authored_by']['author_email']
                authors_by_year_by_dev[dev][str(year)] += 1

        # write out the data rows to the CSV file
        for dev in sorted(devs):
            data_row = [dev]
            total_authored = 0
            for year in list_of_years:
                data_row.append(authors_by_year_by_dev[dev][str(year)])
                total_authored += authors_by_year_by_dev[dev][str(year)]
            data_row.append(total_authored)
            csvwriter.writerow(data_row)
        
        print(f"The list of unique author values has been written to {len(list(devs))}.")


def generate_csv_devs_commit_the_years(input_csv_list, json_obj, output):
    # write out the unique values to the output CSV file
    with open(output, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        list_of_years = get_list_of_years(input_csv_list)
        # write the header row
        header_row = list(list_of_years)
        header_row.insert(0, 'id')
        header_row.append('total_commits')
        csvwriter.writerow(header_row)

        # get the set of unique developers
        devs = set()
        for commit in json_obj["commits"]:
            if 'committed_by' in commit and 'committer_email' in commit['committed_by']:
                dev = commit['committed_by']['committer_email']
                devs.add(dev)

        # create a dictionary to store the number of commits made by each developer in each year
        committers_by_year_by_dev = {
            dev: {str(year): 0 for year in list_of_years} for dev in devs}

        # iterate through the rows of the CSV file and count the number of commits made by each developer in each year
        for commit in json_obj["commits"]:
            if 'committed_by' in commit and 'committer_email' in commit['committed_by']:
                year = get_year_from_date(commit['commited_at'])
                dev = commit['committed_by']['committer_email']
                committers_by_year_by_dev[dev][str(year)] += 1


        # write out the data rows to the CSV file
        for dev in sorted(devs):
            data_row = [dev]
            total_committed = 0
            for year in list_of_years:
                data_row.append(committers_by_year_by_dev[dev][str(year)])
                total_committed += committers_by_year_by_dev[dev][str(year)]
            data_row.append(total_committed)
            csvwriter.writerow(data_row)

        print(f"The list of unique commit values has been written to {len(list(devs))}.")


def get_list_of_years(input_list):
    # create an empty set to store unique values

    years = set()
    for row in input_list[1:]:
        a_at = parser.parse(row[5]).strftime('%m/%d/%Y, %H:%M:%S')
        c_at = parser.parse(row[7]).strftime('%m/%d/%Y, %H:%M:%S')
        authored_at = datetime.datetime.strptime(a_at, '%m/%d/%Y, %H:%M:%S')
        committed_at = datetime.datetime.strptime(c_at, '%m/%d/%Y, %H:%M:%S')
        years.add(authored_at.year)
        years.add(committed_at.year)

    list_of_years = sorted(list(years))
    return list_of_years


def get_year_from_date(date_string):
    date = datetime.datetime.strptime(date_string, '%m/%d/%Y, %H:%M:%S')
    return date.year
