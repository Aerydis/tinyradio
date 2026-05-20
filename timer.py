#import stuff
from datetime import datetime, timedelta
import time
import pygame

pygame.init()

def calculate_sleep_duration(current_full_time):
    #get current time and calculate next hour mark - 5 seconds
    wake_up_time = (
        (current_full_time.replace(minute=0, second=0, microsecond=0)) + timedelta(hours = 1)
    ) - timedelta(seconds=5)

    #calculate how long to sleep for until the next hour mark
    sleep_duration = (wake_up_time - current_full_time).total_seconds()

    #return
    print(f"sleeping for {sleep_duration} seconds until {wake_up_time.time()}...")
    return sleep_duration

def stop_current_track(current_full_time):
    old_track_name = f"tracks/{(current_full_time.hour - 1) % 24:02}.ogg"
    print(f"stopping {old_track_name}...") 
    pygame.mixer.music.fadeout(5000) #fade out over 5 seconds
    time.sleep(5) #wait for fadeout to finish
    print(f"stopped {old_track_name}!")

    print(f"unloading {old_track_name}...")
    pygame.mixer.music.unload()
    print(f"unloaded {old_track_name}!")

def play_new_track(current_full_time):
    new_track_name = f"tracks/{current_full_time.hour:02}.ogg"
    print(f"loading {new_track_name}...")
    pygame.mixer.music.load(new_track_name)
    print(f"loaded {new_track_name}!")
    
    print(f"playing {new_track_name}...")
    pygame.mixer.music.play(-1)
    print(f"played {new_track_name}!")

#run functions
while True:
    current_full_time = datetime.now()
    play_new_track(current_full_time)
    time.sleep(calculate_sleep_duration(current_full_time))
    stop_current_track(current_full_time)