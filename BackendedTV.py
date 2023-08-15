import socket, asyncio, sys

a = input(" IP[:PORT] > ")

if len(a.split(":")) > 1:
    serverAddressPort   = (a, int(a.split(":")[1]))
else:
    serverAddressPort   = (a, 20001)

uname = input(" Username > ")

msgFromClient       = uname

bytesToSend         = str.encode(msgFromClient)



bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
async def getMessage(string):
    #await asyncio.to_thread(sys.stdout.write, f'{string} ')
    return (await asyncio.to_thread(sys.stdin.readline)).rstrip('\n')
 

msg = "Message from Server {}".format(msgFromServer[0])
# Send to server using created UDP socket
do_it = False
while True:

    #a = asyncio.run(getMessage(" Message > "))
    
    #if a == "!exit":
    #    exit()
   

 

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    if not do_it:
        bytesToSend = str.encode("Data recived by " + uname)
        
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    
    do_it = True

    msg = "{}".format(msgFromServer[0].decode('ascii'))

    print(msg)