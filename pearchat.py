import socket


def receive():
	host = '127.0.0.1'
	port = 5000

	sckt = socket.socket()
	sckt.bind((host, port))

	sckt.listen(1)
	conn, addr = sckt.accept()
	print('Connention from : {}'.format(addr))
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print('Received data: {}'.format(str(data)))

