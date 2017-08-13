import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        rand = str(random.randrange(654654, 25454153))
        await websocket.send(rand)
        await asyncio.sleep(.01)
        print(rand)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
