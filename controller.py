#import stuff
import time
from datetime import datetime 

#import other files
import timer
import player

#run functions
while True:
    current_full_time = datetime.now()
    current_track_name = f"tracks/{current_full_time.hour:02}.ogg"

    player.play_new_track(current_track_name)
    time.sleep(timer.calculate_sleep_duration(current_full_time))
    player.stop_current_track(current_track_name)