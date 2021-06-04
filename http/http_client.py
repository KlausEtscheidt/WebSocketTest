 #!/usr/bin/env python

import urllib.request
import datetime
import logging

logger = logging.getLogger('name')

def send_input():  
    print('http client is connecting...')
    while 1:  
        cmd = input('input command (ex. GET index.html): ')  
        
        if cmd == 'exit': #tipe exit to end it  
            break

        socket_send(cmd)

def socket_send(cmd):
        cmd = bytes( cmd, 'utf-8')
        req = urllib.request.Request(url='http://localhost:8080',
                                    data=cmd, method='POST')

        with urllib.request.urlopen(req) as f:
            logger.info(str(f.read(),'utf-8'))

        logger.debug('%s %s',f.status,f.reason)

def send_numbers():
    for i in range(200):
        socket_send(str(i))

now = datetime.datetime.now()

#logger.setLevel(logging.ERROR)
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
logger.info("Start")
send_numbers()
logger.info(datetime.datetime.now()-now)
input('Ende ...')
