import socket
import zlib
import argparse


def getdata(message):
    length = len(message)

    if len(str(length)) > 16:
        raise Exception('The message is too long! Exiting')

    data = '{:>16}'.format(str(length)).encode('UTF-8') + '{:>10}'.format(str(zlib.crc32(message))).encode('UTF-8') + message
    return data


def send(host, port, message):
    data = getdata(message)

    sckt = socket.socket()
    sckt.connect((host, port))

    totalsent = 0
    while totalsent < len(data):
        sent = sckt.send(data[totalsent:])
        if not sent:
            raise RuntimeError('Socket connection broken!')
        totalsent = totalsent + sent


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


def considerate_print(text=None, quiet=False):
    if not quiet:
        if not text:
            print()
        else:
            print(text)


def receive(host, port, quiet=False):
    considerate_print('[*] Listening for connections on: {host}:{port}'.format(host=host, port=port), quiet)
    
    sckt = socket.socket()
    sckt.bind((host, port))

    sckt.listen(1)
    conn, addr = sckt.accept()
    considerate_print(quiet=quiet)
    considerate_print('[*] Connection from : {addr[0]}:{addr[1]}'.format(addr=addr), quiet)

    chunks = []
    bytes_received = 0
    chunk = conn.recv(16)
    length = int(chunk.decode('UTF-8'))

    checksum = int(conn.recv(10).decode('UTF-8'))
    
    while bytes_received < length:
        chunk = conn.recv(min(length-bytes_received, 1024))
        if not chunk:
            raise RuntimeError('Socket connection broken!')
        chunks.append(chunk)
        bytes_received = bytes_received + len(chunk)

    data = b''.join(chunks)
    if (zlib.crc32(data) != checksum):
        raise RuntimeError("Checksums don't match!")
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help='Whether to send or receive', type=str, choices=['send', 'receive'])
    parser.add_argument('-i', '--interactive', help='If the program is to be run in interactive mode', action='store_true')
    parser.add_argument('-f', '--filepath', help='Path of the file to be sent or to save incoming data to', type=str)
    parser.add_argument('--host', help='Address of the source or target machine', type=str)
    parser.add_argument('-p', '--port', help='Port for listening on or sending to', type=int, default=5000)
    parser.add_argument('-m', '--message', help='Message to send', type=str)
    parser.add_argument('-q', '--quiet', help='Quiet mode', action='store_true')
    args = parser.parse_args()

    if args.mode=='send':
        if args.interactive:
            host = input('[?] The address of the target machine: ')
            port = int(input('[?] Enter the port to connect to: ') or '5000')
            filename = input('[?] The file to send. Leave blank for text message: ')
        else:
            host = args.host
            port = int(args.port or '5000')
            filename = args.filepath
        
        if filename:
            with open(filename, 'rb') as f:
                message = f.read()
        else:
            message = args.message.encode('UTF-8')
            if not message:
                message = input('[?] Enter the message: ').encode('UTF-8')

        send(host, port, message)
        considerate_print(quiet=args.quiet)
        considerate_print('[*] Sent message succesfully!', args.quiet)

    elif args.mode=='receive':
        if args.interactive:
            port = int(input('[?] Port to listen on: ') or '5000')
            destination = input('[?] File to save the incoming data to. Leave blank to output to terminal: ')
        else:
            port = args.port or '5000'
            destination = args.filepath

        try:
            message = receive(get_ip(), port, args.quiet)
        except RuntimeError as e:
            considerate_print('[!] RuntimeError: {}'.format(e), args.quiet)
            sys.exit(1)

        if destination:
            with open(destination, 'wb') as f:
                f.write(message)
            considerate_print('[*] Incoming data saved to {}'.format(destination), args.quiet)
        else:
            considerate_print('[*] The incoming data is > ', args.quiet)
            print(message)


if __name__=='__main__':
    main()
