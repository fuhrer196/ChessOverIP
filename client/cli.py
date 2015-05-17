import socket

host = 'google.com'
port = 5000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##print "yaha obv"
s.connect((host,port))
##print "yaha pohoncha toh stud"
s.send('To the world, Hello I say')
##print "machaya"
data = s.recv(size)
print data
while 1:
    data=raw_input('Manan : ')
    s.send(data)
    if data=='exit()':
        break
    data = s.recv(size)
    if data=='exit()':
        break
    print "Khujao : " + data
##print "Toh phir problem kya hein?"
s.close()
print 'Received:', data
