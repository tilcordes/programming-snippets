import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.178.49', 1887))
server_socket.listen(1)

while True:
    connection, address = server_socket.accept()
    print(connection.recv(512).decode())
    connection.send('Message from server'.encode())