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

        years_ago = time_difference.days // 365
        months_ago = time_difference.days // 30
        days_ago = time_difference.days
        hours_ago = time_difference.seconds // 3600
        minutes_ago = (time_difference.seconds % 3600) // 60
        seconds_ago = time_difference.seconds % 60

        if years_ago > 0:
            print(f"{past_time} was {years_ago} years ago.")
        elif months_ago > 0:
            print(f"{past_time} was {months_ago} months ago.")
        elif days_ago > 0:
            print(f"{past_time} was {days_ago} days ago.")
        elif hours_ago > 0:
            print(f"{past_time} was {hours_ago} hours ago.")
        elif minutes_ago > 0:
            print(f"{past_time} was {minutes_ago} minutes ago.")
        else:
            print(f"{past_time} was {seconds_ago} seconds ago.")
        print()

print_time_difference()
