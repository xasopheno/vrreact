import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        now = str(random.randrange(654654, 25454153))
        await websocket.send(now)
        await asyncio.sleep(random.random())

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
