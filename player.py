import pygame
import time

pygame.init()

current_track_name = ""
old_track_name = ""

def play_new_track(current_full_time):
    global current_track_name
    current_track_name = f"tracks/{current_full_time.hour:02}.ogg"
    print(f"loading {current_track_name}...")
    pygame.mixer.music.load(current_track_name)
    print(f"loaded {current_track_name}!")
    
    print(f"playing {current_track_name}...")
    pygame.mixer.music.play(-1)
    print(f"now playing {current_track_name}!")

def stop_current_track():
    global old_track_name
    global current_track_name
    old_track_name = current_track_name
    print(f"stopping {old_track_name}...") 
    pygame.mixer.music.fadeout(5000) #fade out over 5 seconds
    time.sleep(5) #wait for fadeout to finish
    print(f"stopped {old_track_name}!")

    print(f"unloading {old_track_name}...")
    pygame.mixer.music.unload()
    print(f"unloaded {old_track_name}!")