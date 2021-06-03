# WS client example

import asyncio
import websockets
import datetime

async def sendmsg(msg):
    uri = "ws://localhost:8889"
    async with websockets.connect(uri) as websocket:

        await websocket.send(msg)

        greeting = await websocket.recv()
        print(greeting)

def socket_send(msg):
    asyncio.get_event_loop().run_until_complete(sendmsg(msg))

def name_send():
    while True:
        name = input("What's your name? ")
        socket_send(name)

def send_numbers():
    for i in range(200):
        socket_send(str(i))

now = datetime.datetime.now()
print(now)
send_numbers()
print(datetime.datetime.now()-now)
input('Ende ...')