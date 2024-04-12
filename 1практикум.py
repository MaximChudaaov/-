import os
import json

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