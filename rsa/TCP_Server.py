import socket

#Global variables
d = 103 #Private Key
n = 169 #Public Key
e = 7 #Constant exponent
flag = b"{{flag}}"

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ensure that you can restart your server quickly when it terminates
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set the client socket's TCP "well-known port" number
well_known_port = 5000
sock.bind(('', well_known_port))

# Set the number of clients waiting for connection that can be queued
sock.listen(5)

# This method on the server to validate the signature they provide
def verify(x):
    signature = x
    msg = "Hello!".encode('utf8')
    hash = int.from_bytes(msg, byteorder='big')%n
    
    hashFromSignature = pow(signature, d, n)
    print("Hash: ", hash)
    print("Hash from Signature: ", hashFromSignature)
    print("Signature Int: ", signature)
    print("Signature valid:", hash == hashFromSignature)
    return (hash == hashFromSignature)

# loop waiting for connections (terminate with Ctrl-C)
try:
    while True:
        newSocket, address = sock.accept()
        print("Connected from", address)
        newSocket.send(b"Hi Shamir sign this message to verify:\n")
        newSocket.send(b"Hello!\nAwaiting Response...\n")
        # loop serving the new client
        while True:
            receivedData = newSocket.recv(1024)
            if not receivedData: break
            
            msg_recv = receivedData.decode()
            try:
                # interpret the input as a base-16 number, a hexadecimal
                user_sign = int(msg_recv, 16)
                
                result = verify(user_sign)
    
                # Echo back the verification result
                if result is True:
                    newSocket.send(b"Signature is Valid\n")
                    newSocket.send(b"Here is your flag:"+flag + b"\n")
                    #send flag to user here
                
                    break
                else:
                    newSocket.send(b"Signature is not Valid\n")
            except ValueError:
                newSocket.send(b"Signature is not Valid!\n")
                newSocket.send(b"Awaiting Response...\n")
                continue
            
        newSocket.close()
        print("Disconnected from", address)
finally:
    sock.close()

    
