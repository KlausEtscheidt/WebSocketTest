# WS client example

import asyncio
import websockets

async def sendmsg(msg):
    uri = "ws://192.168.111.36:8889"
    async with websockets.connect(uri) as websocket:

        await websocket.send(msg)

        greeting = await websocket.recv()
        print(greeting)



while True:
    name = input("What's your name? ")
    asyncio.get_event_loop().run_until_complete(sendmsg(name))
    
