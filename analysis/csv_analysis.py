import csv
import os
from utils.file_utils import save_path

def analyze_data_devs(data, columns, row_index, output):
    # create an empty set to store unique values
    unique_authors = set()
    unique_committers = set()

    # read in the CSV data and iterate over each row
    for row in data[row_index:]:
        # add each value in the specified column to the set of unique values
        unique_authors.add(row[columns[0]])
        unique_committers.add(row[columns[1]])

    # count the number of unique values
    num_unique_authors = len(unique_authors)
    num_unique_committers = len(unique_committers)

    # write out the unique values to the output CSV file
    with open(output, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # write the header row
        csvwriter.writerow(['Authors', 'Committer'])
        # write each unique value as a row in the output CSV file
        for a, c in zip(unique_authors, unique_committers):
            csvwriter.writerow([a, c])


    output_file_name = os.path.basename(output)

    print(f"There are {num_unique_authors} unique values in column {1}.")
    print(f"The list of unique values has been written to {output_file_name}.")
    print(f"There are {num_unique_committers} unique values in column {2}.")
    print(f"The list of unique values has been written to {output_file_name}.")

    return num_unique_authors, num_unique_committers
