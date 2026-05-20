import pygame
import time

pygame.init()

def play_new_track(current_track_name):
    print(f"loading {current_track_name}...")
    pygame.mixer.music.load(current_track_name)
    print(f"loaded {current_track_name}!")

    print(f"playing {current_track_name}...")
    pygame.mixer.music.play(-1)
    print(f"now playing {current_track_name}!")

def stop_current_track(current_track_name):
    print(f"stopping {current_track_name}...") 
    pygame.mixer.music.fadeout(5000) #fade out over 5 seconds
    time.sleep(5) #wait for fadeout to finish
    print(f"stopped {current_track_name}!")

    print(f"unloading {current_track_name}...")
    pygame.mixer.music.unload()
    print(f"unloaded {current_track_name}!")