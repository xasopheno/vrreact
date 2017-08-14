import asyncio
import datetime
import random
import websockets
import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

with open('./src/Server/ip.json', 'w') as outfile:
    json.dump({'ip': ip}, outfile)

async def time(websocket, path):
    while True:
        rand = str(random.randrange(0, 23443212325454111239823498743298729871092873444322342153254541112344322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153234432123254541112398234987432987298710928734443223421532344321232545411123982349874329872987109287344432234215323443212325454111239823498743298729871092873444322342153))
        await websocket.send(rand)
        await asyncio.sleep(.01)
        print(rand)

start_server = websockets.serve(time, ip, 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
