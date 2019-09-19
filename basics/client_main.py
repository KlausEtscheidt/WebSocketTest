import socket
import sys
port =8889
print('----------sending to port ',port,' ---------------')
def socket_send(token):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', port)
    print ( 'connecting to %s port %s' % server_address)
    sock.connect(server_address)

    try:
        
        # Send data
        message = bytes("{}".format(token), 'ascii')
        #message=token
        print ('sending {}'.format( message))
        sock.sendall(message)

        # Look for the response
        amount_received = 1

        heard=''
        while  amount_received > 0:
            data = sock.recv(8)
            amount_received = len(data)
            heard+=str(data,'ascii')

        print ('received "%s"' % heard)
    except:
        print("Fehler: {}".format(sys.exc_info()))

    finally:
        print ( 'closing socket')
        sock.close()

def menu():
    tokens=("Status","Pumpenstatus","Pumpe Pumpe ein","Pumpe Pumpe aus","Pumpe Ventil1 auf","Pumpe Ventil1 zu","Pumpe Ventil2 auf","Pumpe Ventil2 zu")
    tokens+= ("Sensorwert T_GH_aus","Sensorwert Bar_GH_aus_Druck","Sensorwert Bar_GH_aus_T","Sensorwert Hyg_GH_aus_Hum","Sensorwert Hyg_GH_aus_T")
    tokens+= ("Sensorwert T_GH_innen_T","Sensorwert T_GH_Boden_T","Stop")

    wahl=0
    
    while not wahl == 99:
        i=1
        for token in tokens:
            print (i,token)
            i+=1

        print ("99","Ende")

        wahl=int(input(''))

        if not wahl == 99:
            token=tokens[wahl-1]
            print (token)
            socket_send(token)

def testbytes():
    import struct

    t1=0xFD
    t2=0x04
    t3=1
    msg=struct.pack("3B4s",t1,t2,t3,bytes("text","utf-8"))
    #msg=struct.pack("BhB",t2,t3)
    for byte in msg:
       print(byte)
    print("len ",len(msg))   
    print ('sending {}'.format( msg))
    socket_send(msg)
menu()
#testbytes()    
