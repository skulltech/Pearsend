def getdata(message, maxlength):
	message = message.encode('UTF-8')
	length = len(message)

	if length > maxlength:
		raise Exception('The message is too long! Exiting')

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
	# host = input('Enter host address of the target machine: ')
	# port = input('Enter the port to connect to: ')
	message = input('Enter the message: ')

	send('127.0.0.1', 5000, message)
