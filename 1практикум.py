import os
import json
import socket


def get_file_info(dir_path):
    file_info = {}
    for root, dirs, files in os.walk(dir_path):
        file_info[root] = []
        for file in files:
            file_path = os.path.join(root, file)
            file_info[root].append(file_path)
    return file_info

dir_path = os.getcwd()
file_info = get_file_info(dir_path)

with open('file_info.json', 'w') as f:
    json.dump(file_info, f, indent=4)

def handle_command(command):
    if command.startswith("set_root_folder"):
        new_root_folder = command.split()[1]
        file_info = get_file_info(new_root_folder)
        with open('new_file_info.json', 'w') as f:
            json.dump(file_info, f, indent=4)
        return "New root folder set and file info saved."
    else:
        return "Invalid command."


s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    command = c.recv(1024).decode()
    response = handle_command(command)
    c.send(response.encode())
    c.close()
