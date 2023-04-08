def get_column(data, index):
    """Returns a column from a list of lists."""
    column = [row[index] for row in data]
    return column

def count_unique_values(column):
    """Counts the number of unique values in a list."""
    unique_values = set(column)
    num_unique_values = len(unique_values)
    return num_unique_values

def clean_data(data):
    """Cleans the data by removing any empty or invalid rows."""
    cleaned_data = [row for row in data if all(row)]
    return cleaned_data

def clean_data_lowercase(data):
    """
    Clean and preprocess data by removing any empty rows and columns,
    and converting all string data to lowercase.
    """
    # Remove empty rows
    data = [row for row in data if any(row)]

    # Remove empty columns
    data = [list(filter(None, row)) for row in zip(*data) if any(row)]

    # Convert all string data to lowercase
    data = [[cell.lower() if isinstance(cell, str) else cell for cell in row] for row in data]

    return data