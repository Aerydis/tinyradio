#import stuff
import time
from datetime import datetime 

#import other files
import timer
import player

#run functions
while True:
    current_full_time = datetime.now()
    player.play_new_track(current_full_time)
    time.sleep(timer.calculate_sleep_duration(current_full_time))
    player.stop_current_track()