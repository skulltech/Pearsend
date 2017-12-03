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


def receive():
	host = get_ip()
	# host = socket.gethostbyname(socket.gethostname())
	# host = '127.0.0.1'
	print(host)
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
