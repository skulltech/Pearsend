import socket
import zlib


def getdata(message):
	length = len(message)

	if len(str(length)) > 16:
		raise Exception('The message is too long! Exiting')

	data = '{:>16}'.format(str(length)).encode('UTF-8') + '{:>10}'.format(str(zlib.crc32(message))).encode('UTF-8') + message
	return data


def send(host, port, message):
	data = getdata(message)
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
	host = input('[?] The address of the target machine: ')
	port = int(input('[?] Enter the port to connect to: ') or '5000')
	filename = input('[?] The file to send. Leave blank for text message: ')

	if filename:
		with open(filename, 'rb') as f:
			message = f.read()
	else:
		message = input('[?] Enter the message: ').encode('UTF-8')

	send(host, port, message)
	print()
	print('[*] Sent message succesfully!')


if __name__=='__main__':
	main()
