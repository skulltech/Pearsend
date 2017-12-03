# PearSend
A simple CLI client for peer-to-peer file or message sending. Written in Python.

## Features

- It supports file or message of size upto about 8.85 PeB (1 PiB ~ 10^6 GiB)!.
- Protection against transmission error using `CRC32` checksum.
- Comes with CLI (command-line argument) and Interactive mode, both!

# Usage Examples

## Command-line Mode

__Help Text__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py -h
usage: pearsend.py [-h] [-i] [-f FILEPATH] [--host HOST] [-p PORT]
                   [-m MESSAGE]
                   {send,receive}

positional arguments:
  {send,receive}        Whether to send or receive

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     If the program is to be run in interactive mode
  -f FILEPATH, --filepath FILEPATH
                        Path of the file to be sent or to save incoming data
                        to
  --host HOST           Address of the source or target machine
  -p PORT, --port PORT  Port for listening on or sending to
  -m MESSAGE, --message MESSAGE
                        Message to send
```

### Sending text message

__Receiver__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py receive -p 5000
[*] Listening for connections on: 10.194.52.135:5000

[*] Connection from : 10.194.52.135:47804
[*] The incoming data is > 
b'Hello HAL!'
```

__Sender__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py send --host 10.194.52.135 -m "Hello HAL!"

[*] Sent message succesfully!
```

### Sending binary file

__Receiver__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py receive -p 5000 -f recd.png
[*] Listening for connections on: 10.194.52.135:5000

[*] Connection from : 10.194.52.135:47808
[*] Incoming data saved to recd.png
```

__Sender__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py send --host 10.194.52.135 -f image.png

[*] Sent message succesfully!
```


## Interactive Mode

### Sending text message 

__Receiver__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py receive -i
[?] Port to listen on: 
[?] File to save the incoming data to. Leave blank to output to terminal: 
[*] Listening for connections on: 10.194.52.135:5000

[*] Connection from : 10.194.52.135:36240
[*] The incoming data is > 
b'Hello HAL!'
```

__Sender__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py send -i
[?] The address of the target machine: 10.194.52.135
[?] Enter the port to connect to: 
[?] The file to send. Leave blank for text message: 
[?] Enter the message: Hello HAL!

[*] Sent message succesfully!
```

### Sending binary file

__Receiver__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py receive -i
[?] Port to listen on: 
[?] File to save the incoming data to. Leave blank to output to terminal: recd.jpg
[*] Listening for connections on: 10.194.52.135:5000

[*] Connection from : 10.194.52.135:36242
[*] Incoming data saved to recd.jpg
```

__Sender__
```terminal
sumit@HAL9000:~/Documents/PearSend$ python3 pearsend.py send -i
[?] The address of the target machine: 10.194.52.135
[?] Enter the port to connect to: 
[?] The file to send. Leave blank for text message: image.jpg

[*] Sent message succesfully!
```
