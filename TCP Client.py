import socket

target_host = "127.0.0.1"
target_port = 9998

#create a socket object, AF_INET indicates standard IPV4 Addressing or hostname.
#SOCK_STREAM indicates using a TCP client socket type.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client, send data as bytes.
client.connect((target_host,target_port))

#send some data
client.send(b"GET / HTTP/1.1\r/nHost: google.com\r\n\r\n")

#recieve some data
response = client.recv(4096)

print(response.decode())
client.close()