import os
import shutil

path = "/Users/jackie/Downloads"

if not os.path.exists(path):
    exit()

os.chdir(path)
file_list = os.listdir("./")
# print(file_list)

for file_name in  file_list:
    print(file_name)

