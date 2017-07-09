import socket
import sys


HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])



while(True):
	# Create a socket (SOCK_STREAM means a TCP socket)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect to server and send data
	sock.connect((HOST, PORT))
	data = input(">>")
	sock.sendall(bytes(data + "\n", "utf-8"))
	received = str(sock.recv(1024), "utf-8")
	print("Received: {}".format(received))
	sock.close()

# Receive data from the server and shut down
received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))