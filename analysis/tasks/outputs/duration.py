import datetime


def calculate_duration(authored_at, committed_at):
    """
    Calculates the duration between the authored_at and committed_at times.
    Returns a float representing the duration in days.
    """
    authored_time = datetime.datetime.strptime(authored_at, '%m/%d/%Y, %H:%M:%S')
    committed_time = datetime.datetime.strptime(committed_at, '%m/%d/%Y, %H:%M:%S')
    duration = committed_time - authored_time
    return duration.days