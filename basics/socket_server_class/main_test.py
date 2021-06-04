#!/usr/bin/env python3

#################################################################
#
# Hauptprogramm zum Test des Socket-Servers
#
#################################################################

#import time,sys,logging,os,signal

from socket_server import KE_socket_listener, KE_ThreadedTCPRequestHandler

#Die Methode cmd_handler von KE_ThreadedTCPRequestHandler muss überschrieben werden
#Der Befehl stop wird von der Basisklasse behandelt und beendet die Kommunikation
class RQHandler(KE_ThreadedTCPRequestHandler):
    def cmd_handler(self, command):
        print('Got here ------ <{}>'.format(command))

class Test:
    def __init__(self):

        #Startet socketserver in eigenem thread
        host = '127.0.0.1'
        port = 8887
        socket_input=KE_socket_listener(self, host, port, RQHandler)

        #Endlos nur zur Demo, damit main nicht endet
        while True:
            #Abbruch uber Socket gefordert ?
            if socket_input.server.stop:
                break
        socket_input.close()

Test()
pass

