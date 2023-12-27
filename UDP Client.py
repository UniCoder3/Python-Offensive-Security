import socket

target_host = "127.0.0.1"
target_port = 9997

#create a socket object, AF_INET indicates standard IPV4 Addressing or hostname.
#SOCK_DGRAM indicates using a UDP socket type. 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))

#recieve some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()