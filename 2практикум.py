import socket
import json

def send_command(command):
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((host, port))
    s.send(command.encode())
    response = s.recv(1024)
    s.close()

    return response.decode()

command = r"C:\Users\maxim\Desktop"
response = send_command(command)
print(response)