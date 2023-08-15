import socket, asyncio, sys, _thread

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
def getUserMessagesLoop():
    while True:
        getOtherUserMessage()
        bytesToSend = str.encode("Data recived by " + uname)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

def getOtherUserMessage():
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = "{}".format(msgFromServer[0].decode('ascii'))

    print(msg)
    
_thread.start_new_thread(getUserMessagesLoop,tuple([]))
while True:
    
    a = asyncio.run(getMessage(" Message > "))
    
    if a == "!exit":
        exit()
   
    bytesToSend = str.encode("[" + uname + "]: " + a)
        
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
 

    #getOtherUserMessage()