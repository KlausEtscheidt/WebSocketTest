# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print("<{}>".format(name))

    greeting = "Hello "+ name

    await websocket.send(greeting)
    print(greeting)

#start_server = websockets.serve(hello, "127.0.0.1", 8889)
start_server = websockets.serve(hello, "localhost", 8889)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
