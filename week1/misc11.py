import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('115.29.77.78',9979))
import time
sock11=sock.recv(1024)
print sock11
sock11=sock.recv(1024)
print sock11
pos2=sock11.find('=',950)
sendr = eval(sock11[945:pos2])
print sendr
sock.send(repr(sendr)+'\n')
while 1:
	sock11=sock.recv(1024)
	print sock11
	pos=sock11.find('=')
	i=sock11.find(']')
	if(i!=-1):
		sendr=eval(sock11[i+2:pos].replace('\xc3\x97','*'))
		print sendr
		sock.send(repr(sendr)+'\n')
	else:
		sendr=eval(sock11[:pos])
		print sendr
		sock.send(repr(sendr)+'\n')
sock.close()
