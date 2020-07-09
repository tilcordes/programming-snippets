import socket

port = 1887
ip = '192.168.178.49'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))
client_socket.send('Message from client'.encode())
print(client_socket.recv(512).decode())