import socket

# Annoyingly, due to the way that Backended is programmed, it can't asyncronously get messages from the server while allowing user input.

a = input("Port number (default 20001) > ")

b = input("Host IP (leave blank if using localhost test) > ")

if a == "":
    localPort   = 20001
else:
    localPort   = int(a)

if b == "":
    localIP     = "127.0.0.1"
else:
    localIP = b


bufferSize  = 1024

msgFromServer       = "Connection established."

bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

clients = []

# Listen for incoming datagrams

messageBacklog = b""

while(True):
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message.decode('ascii'))
        #clientIP  = "Client IP Address:{}".format(address)
    
        if message == b'!fcloseserver':
            exit()
    
        print(clientMsg)
    except:
        print("Warning: Could not recieve user content.")
    #print(clientIP)
    # Sending a reply to client
    hasClientFound = False
    for e in clients:
        if address == e:
            hasClientFound = True
    if not hasClientFound:
        UDPServerSocket.sendto(bytesToSend, address)
        clients.append(address)
        UDPServerSocket.sendto(b'Welcome to the server, ' + message + b'!', address)
    else:
        if not message.startswith(b"Data recived by "):
            UDPServerSocket.sendto(message, address)
            print(clients)
            for add in clients:
                try:
                    if add != address:
                        UDPServerSocket.sendto(message, add)
                except:
                    print("Warning: Couldn't send message to " + add[0])