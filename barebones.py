#import stuff
from datetime import datetime
import asyncio

#print the time every second
async def main():
    while True:
        timenow = datetime.now()
        print("The current time is:", timenow)
        await asyncio.sleep(1)
        print("The current hour is:", timenow.hour)

#run
asyncio.run(main())