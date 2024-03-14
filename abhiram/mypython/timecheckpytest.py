import pytest
from datetime import datetime

# Function to calculate time difference
def print_time_difference(past_time_str):
    current_time = datetime.now()
    past_time = datetime.strptime(past_time_str, "%Y-%m-%d %H:%M:%S")
    time_difference = current_time - past_time

    # Calculate time difference in seconds, minutes, hours, days, and months
    seconds_ago = time_difference.total_seconds()
    minutes_ago = seconds_ago // 60
    hours_ago = minutes_ago // 60
    days_ago = time_difference.days
    months_ago = days_ago // 30  # Assuming a month is 30 days on average

    # Calculate years ago
    years_ago = current_time.year - past_time.year
    if (current_time.month, current_time.day) < (past_time.month, past_time.day):
        years_ago -= 1

    # Calculate months ago
    months_ago = current_time.month - past_time.month
    if months_ago < 0:
        months_ago += 12
        years_ago -= 1

    # Adjust days ago based on months and years
    past_time = past_time.replace(year=current_time.year, month=current_time.month)
    days_ago = (current_time - past_time).days

    # Adjust other time units based on months and years
    hours_ago -= days_ago * 24
    minutes_ago -= hours_ago * 60
    seconds_ago -= minutes_ago * 60

    return (years_ago, months_ago, days_ago, hours_ago, minutes_ago, seconds_ago)

# Test function using pytest and mark.parametrize
@pytest.mark.parametrize("past_time_str, expected_output", [
    ("2023-03-01 12:00:00", (0, 11, 6, 9, 41, 10)),
    ("2022-10-15 08:30:00", (1, 4, 22, 15, 11, 10)),
    ("2021-12-25 18:45:00", (2, 2, 10, 9, 56, 10)),
    ("2020-07-07 09:15:00", (3, 8, 28, 15, 41, 10)),
    ("2019-01-01 00:00:00", (5, 2, 7, 18, 56, 10))
])
def test_print_time_difference(past_time_str, expected_output):
    years_ago, months_ago, days_ago, hours_ago, minutes_ago, seconds_ago = print_time_difference(past_time_str)
    assert (years_ago, months_ago, days_ago, hours_ago, minutes_ago, round(seconds_ago)) == expected_output
