import asyncio
import datetime
import random
import websockets

async def cmd_handler(cmd):
   print("Bekam <{}>".format(cmd))
   return(cmd)

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        name = await websocket.recv()
        print("------{}------".format(name))
        await asyncio.sleep(random.random() * 10)

async def echo(websocket, path):
    #print(websocket)
    #print(dir(websocket))
    #while True:   
    cmd=await websocket.recv()
    await cmd_handler(cmd)
    await websocket.send('bekam '+cmd)

#start_server = websockets.serve(time, "127.0.0.1", 8889)
start_server = websockets.serve(echo, "127.0.0.1", 8889)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
