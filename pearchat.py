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
	chunk = sckt.recv(4)
	length = int(chunk.decode('UTF-8'))

	while bytes_received < length:
		chunk = conn.recv(min(length-bytes_received, 1024)).decode()
		if not chunk:
			raise RuntimeError('Socket connection broken!')
		chunks.append(chunk)
		bytes_received = bytes_received + len(chunk)

	return b''.join(chunks).decode('UTF-8')

def getdata(message, maxlength):
	message = message.encode('UTF-8')
	length = len(message)

	if length > maxlength:
		print('The message is too long! Exiting')
		sys.exit()

	data = {:0^4}.format(str(len(message))).encode('UTF-8') + message
	return data


def send(host, port, message):
	data = getdata(message, 4)
	length = len(data)

	sckt = socket.socket()
	sckt.connect((host, port))

	totalsent = 0
	while totalsent < length:
		sent = sckt.send(data[totalsent:])
		if not sent:
			raise RuntimeError('Socket connection broken!')
		totalsent = totalsent + sent


def main():
	host = input('Enter host address of the target machine: ')
	port = input('Enter the port to connect to: ')

	sckt = socket.socket()
	sckt.connect((host, port))
