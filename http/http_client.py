#!/usr/bin/env python

import urllib.request

def run():  
    print('http client is connecting...')
    while 1:  
        cmd = input('input command (ex. GET index.html): ')  
        
        if cmd == 'exit': #tipe exit to end it  
            break  

        #cmd = bytes( "{}".format(cmd), 'ascii')
        cmd = bytes( cmd, 'ascii')
        req = urllib.request.Request(url='http://localhost:8080',
                                    data=cmd, method='POST')

        with urllib.request.urlopen(req) as f:
            print(str(f.read(),'ascii'))

        #print('headers: {}'.format(f.headers))
        print(f.status,f.reason)


if __name__ == '__main__':
  run()
