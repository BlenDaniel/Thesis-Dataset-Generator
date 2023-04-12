import datetime

def get_year(timestamp):
    year = datetime.datetime.strptime(timestamp, '%m/%d/%Y, %H:%M:%S').year
    return str(year)

def categorize_time(timestamp):
    hour = datetime.datetime.strptime(timestamp, '%m/%d/%Y, %H:%M:%S').hour
    if 0 <= hour < 6:
        return 1  # 00:00-06:00AM
    elif 6 <= hour < 12:
        return 2  # 06:00-12:00
    elif 12 <= hour < 18:
        return 3  # 12:00-18:00
    else:
        return 4  # 18:00-23:59


def categorize_season(timestamp):
    month = datetime.strptime(timestamp, '%m/%d/%Y, %H:%M:%S').month
    if 3 <= month <= 5:
        return 1  # Spring
    elif 6 <= month <= 8:
        return 2  # Summer
    elif 9 <= month <= 11:
        return 3  # Fall
    else:
        return 4  # Winter
