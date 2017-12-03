import socket
import sys


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def receive(host, port):
	print('Listening for connections on: {host}:{port}'.format(host=host, port=port))
	
	sckt = socket.socket()
	sckt.bind((host, port))

	sckt.listen(1)
	conn, addr = sckt.accept()
	print('Connection from : {}'.format(addr))

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

	return b''.join(chunks)

def main():
	port = int(input('Port to listen on: ') or '5000')
	destination = input('File to save the incoming data to: ')

	message = receive(get_ip(), port)
	if destination:
		with open(destination, 'wb') as f:
			f.write(message)
	else:
		print(message)


if __name__=='__main__':
	main()
