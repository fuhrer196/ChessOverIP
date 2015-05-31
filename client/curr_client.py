import socket               # Import socket module

def updateBoard(board, move):
    return
    
def playGame(conn):
    board = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
    # Receive stuff to figure out allthe initial settings and shit
    position = 'white/black'
    if position == 'white':
        server_message = conn.recv(1024)
        if server_message == 'Move':
            conn.send(getValidMove(board,position))
    elif position == 'black':
        move = conn.recv(1024)
        updateBoard(board, move)
        server_message = conn.recv(1024)
        if server_message == 'Move':
            conn.send(getValidMove(board,position))
    while server_message != 'Game Over':
        move = conn.recv(1024)
        updateBoard(board, move)
        server_message = conn.recv(1024)
        if server_message == 'Move':
            conn.send(getValidMove(board, position))
def Main():
    
    s = socket.socket()         # Create a socket object
    host = '192.168.0.124'  # Get local machine name
    port = 5001               # Reserve a port for your service.

    ##print 'yaha to aya'
    s.connect((host, port))
    sent = s.recv(1024)
    while sent:
        print 'Specify ' + sent
        pref = raw_input('>>')
        if s.send(pref):
            print 'Sent:', pref
        sent = s.recv(1024)
    
    print 'All settings complete'
    
    ##print 'yay'
    ## playGame(s)
    s.close

if __name__ == '__main__':
    Main()
