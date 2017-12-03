import socket
import sys


def receive():
	host = '127.0.0.1'
	port = 5000

	sckt = socket.socket()
	sckt.bind((host, port))

	sckt.listen(1)
	conn, addr = sckt.accept()
	print('Connention from : {}'.format(addr))

	chunks = []
	bytes_received = 0
	chunk = conn.recv(4)
	length = int(chunk.decode('UTF-8'))

	while bytes_received < length:
		chunk = conn.recv(min(length-bytes_received, 1024))
		if not chunk:
			raise RuntimeError('Socket connection broken!')
		chunks.append(chunk)
		bytes_received = bytes_received + len(chunk)

	return b''.join(chunks).decode('UTF-8')

def main():
	message = receive()
	print(message)


if __name__=='__main__':
	main()
