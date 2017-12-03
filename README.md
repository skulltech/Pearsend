# PearSend
A simple CLI peer-to-peer chat client written in Python

It supports file or message of size upto about 95 MB only (95.3674 MB to be exact).


## Usage Examples

### Sending text message 

__Receiver__
```terminal
sumit@HAL9000:~/Documents/PearChat$ python3 receiver.py 
[?] Port to listen on: 
[?] File to save the incoming data to. Leave blank to output to terminal: 
[*] Listening for connections on: 10.194.52.135:5000

[*] Connection from : 10.194.52.135:36240
[*] The incoming data is > 
b'Hello HAL!'
```

__Sender__
```terminal
sumit@HAL9000:~/Documents/PearChat$ python3 sender.py 
[?] The address of the target machine: 10.194.52.135
[?] Enter the port to connect to: 
[?] The file to send. Leave blank for text message: 
[?] Enter the message: Hello HAL!

[*] Sent message succesfully!
```

### Sending binary file

__Receiver__
```terminal
sumit@HAL9000:~/Documents/PearChat$ python3 receiver.py 
[?] Port to listen on: 
[?] File to save the incoming data to. Leave blank to output to terminal: recd.jpg
[*] Listening for connections on: 10.194.52.135:5000

[*] Connection from : 10.194.52.135:36242
[*] Incoming data saved to recd.jpg
```

__Sender__
```terminal
sumit@HAL9000:~/Documents/PearChat$ python3 sender.py 
[?] The address of the target machine: 10.194.52.135
[?] Enter the port to connect to: 
[?] The file to send. Leave blank for text message: image.jpg

[*] Sent message succesfully!
```
