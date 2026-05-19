#import stuff
from datetime import datetime
import time

#print the time every second
def get_hour():
    timenow = datetime.now()
    return timenow.hour

def create_filename():
    hournow = get_hour()
    filename = f"tracks/{hournow:02}.mp3"
    return filename

def play():
    filename = create_filename()
    print(f"Playing {filename}...")

#run functions
while True:
    hournow = get_hour()
    time.sleep(1)
    if hournow != get_hour():
        print(f"New hour, playing new track... (time: {datetime.now().hour:02})")
        play()
    else:
        print(f"Same hour, waiting... (time: {datetime.now().hour:02})")
