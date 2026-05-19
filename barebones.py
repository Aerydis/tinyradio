#import stuff
from datetime import datetime, timedelta
import time

def calculate_sleep_duration(current_full_time):
    #get current time and calculate next hour mark
    next_hour_mark = (
        (current_full_time.replace(minute=0, second=0, microsecond=0)) + timedelta(hours = 1)
    )

    #calculate how long to sleep for until the next hour mark
    sleep_duration = (next_hour_mark - current_full_time).total_seconds()

    #return
    return sleep_duration

def play_hourly_track(current_full_time):
    old_track_name = f"tracks/{(current_full_time.hour - 1) % 24:02}.mp3"
    print(f"Stopping {old_track_name}...")
    new_track_name = f"tracks/{current_full_time.hour:02}.mp3"
    print(f"Playing {new_track_name}...")

#run functions
while True:
    current_full_time = datetime.now()
    play_hourly_track(current_full_time)
    time.sleep(calculate_sleep_duration(current_full_time))