#import stuff
from datetime import datetime
import time

#print the time every second
def check_time():
    timenow = datetime.now()
    print("The current hour is:", timenow.hour)
    return timenow.hour

def create_filename():
    hournow = check_time()
    filename = f"tracks/{hournow:02}.mp3"
    return filename

def play():
    filename = create_filename()
    print(f"Playing {filename}...")

#run functions
while True:
    play()
    time.sleep(1)