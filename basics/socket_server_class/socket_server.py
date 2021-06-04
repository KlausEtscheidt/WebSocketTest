from abc import ABC, abstractmethod

import socketserver
import sys
import time
import threading

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

#erbt von socketserver(Modul) .BaseRequestHandler(Basisklasse)
class KE_ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        reply=""
        data = str(self.request.recv(1024), 'utf-8')
        #cur_thread = threading.current_thread()
        command=data.strip()
        if command.casefold() =='stop':
            self.server.stop=True
        else:
            self.cmd_handler(command)

        #Antwort senden
        # response = bytes("{}".format(reply), 'utf-8')
        # self.request.sendall(response)

    @abstractmethod
    def cmd_handler(self, command):
        print('Got <{}>'.format(command))

    # def finish(self):
    #     #pass
    #     print("Ende Gelaende")

class KE_ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    #pass
    stop=False
    command=''

class KE_socket_listener:
    '''startet KE_ThreadedTCPServer in eigenem Thread

        KE_ThreadedTCPServer hat die globals stop und command,
        die von KE_ThreadedTCPRequestHandler gesetzt werden können
        Der Handler wird dem Server-Init übergeben.
        Der Server kann vom Handler mit self.server angesprochen werden
    '''

    def __init__(self, host, port, RequestHandler):
        self.host = host
        self.port = port
        for i in range(1,20):
            try:
                #server erst nur anlegen, keine sockets verbinden, damit Eigenschaften gesetzt werden können
                ####self.server = KE_ThreadedTCPServer((host, port), KE_ThreadedTCPRequestHandler, bind_and_activate=False)
                self.server = KE_ThreadedTCPServer((host, port), RequestHandler, bind_and_activate=False)
                # Die Adresse wird normal nach Ende der Kommunikation für eine Zeit reserviert. 
                # Hier: mehrfach verwenden ohne Wartezeit
                #Der for-loop ist daher eigentlich obsolet (hat auch nicht geholfen)
                self.server.allow_reuse_address = True 
                #Socket verbinden
                self.server.server_bind()
                self.server.server_activate()
                break
            except OSError:
                print("{}. Problem beim Socket verbinden".format(i))
                time.sleep(5)

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        #return(server_thread)

        #Endlos
        while True:
            #Abbruch uber Socket gefordert ?
            if self.server.stop:
                break
        self.close()

    def __del__(self):
        self.close()

    def close(self):
        #Beendet thread, wenn nicht mehr gebraucht
        self.server.shutdown()

