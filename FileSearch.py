import os
import shutil

path = "/Users/jackie/Downloads/Python阶段资料"

if not os.path.exists(path):
    exit()

os.chdir(path)
file_list = os.listdir("./")
# print(file_list)

print(os.getcwd())

def file_traverse(file_name, index=0):
    index += 1
    # print("----------> current: " + file_name)
    if os.path.isdir(file_name):
        for sub_file in os.listdir(file_name):
            sub_path = file_name + "/" + sub_file
            print(index * "-" + sub_file)
            file_traverse(sub_path, index)
    else:
        return

file_traverse(path)