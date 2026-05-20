#import stuff
from datetime import timedelta

def calculate_sleep_duration(current_full_time):
    #next hour mark
    next_hour_mark = current_full_time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    #wake up time, which is 5 seconds before next hour mark (time left for fadeout)
    wake_up_time = next_hour_mark - timedelta(seconds=5)

    #calculate how long to sleep for until the next hour mark
    sleep_duration_seconds = (wake_up_time - current_full_time).total_seconds()

    #return
    print(f"sleeping for {sleep_duration_seconds} seconds until {wake_up_time.time()}...")
    return sleep_duration_seconds