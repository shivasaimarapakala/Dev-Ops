from datetime import datetime

def print_time_difference():
    current_time = datetime.now()
    print("Enter past times (YYYY-MM-DD HH:MM:SS) one by one. Enter 'done' when finished:")

    while True:
        past_time_str = input("Enter past time (or 'done' to finish): ")
        if past_time_str.lower() == 'done':
            break

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

        print(f"{past_time} was:")
        if years_ago > 0:
            print(f"{years_ago} years ago.")
        elif months_ago > 0:
            print(f"{months_ago} months ago.")
        elif days_ago > 0:
            print(f"{days_ago} days ago.")
        elif hours_ago > 0:
            print(f"{hours_ago} hours ago.")
        elif minutes_ago > 0:
            print(f"{minutes_ago} minutes ago.")
        else:
            print(f"{seconds_ago} seconds ago.")
        print()

print_time_difference()
