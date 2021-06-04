#import config

#import logging,threading,time
#import time
import socket,sys

global stop
port=8889

print('----------listening on port ',port,' ---------------')
def socket_command_listener():
    global stop
    stop=False
    
    HOST = ''                 # Symbolic name meaning all available interfaces

    if True:  #Forever Wird das gebraucht ???
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, port))
        s.listen(1)
        s.settimeout(500)
        # Forever bis global stop gesetzt  ----
        while not stop:
            print('warte auf verbindung')
            #Hier wird geblockt, d.h auf eingehende Daten gewartet
            #Daher sollte Modul in eigenem thread laufen
            try:
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    data = str(conn.recv(1024), 'ascii')
                    if data:
                        command=data.strip()
                        answer="Bekam: "+command
                        print('command',command)
                        #sende ergebnis
                        conn.sendall( bytes( "{}".format(answer), 'ascii') )
                    #conn.close()
                    if (command=='Stop'):
                        s.close()
                        print("client fordert Ende")
                        break #Ende forever
            except socket.timeout:
                pass
            except:
                print("Fehler: {}".format(sys.exc_info()))
            if stop:
                s.close()
                break #Ende forever
        print("leaving Socket_listener")
   
if __name__ == '__main__':
    print ('in main')
    socket_command_listener()
    print ('verlasse main')
