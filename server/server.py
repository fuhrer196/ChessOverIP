import socket               # Import socket module

def Main():
            
    s = socket.socket()         # Create a socket object
    host = '0.0.0.0'            # Get local machine name
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(1)                 # Now wait for client connection.
    c, addr = s.accept()     # Establish connection with client.
    print 'Got chat invite from', addr
    c.send('Thank you for connecting')
    data = c.recv(1024)
    data = c.recv(1024)
    while data != 'exit()':
       print 'Manan: ', data
       reply = raw_input('')
       c.send(reply)
       if reply == 'exit()':
           break
       data = c.recv(1024)
    c.close()                # Close the connection
    print 'Connection Closed.'

if __name__ == '__main__':
    Main()
