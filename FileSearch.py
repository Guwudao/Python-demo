import os
import shutil

path = "/Users/jackie/Downloads/Python阶段资料/01-学前阶段"

if not os.path.exists(path):
    exit()

os.chdir(path)
file_list = os.listdir("./")
print(file_list)

print(os.getcwd())

def file_traverse(file_name, index=0):
    index += 1
    if os.path.isdir(file_name):
        for sub_file in os.listdir(file_name):
            print(index * "-" + sub_file)
            # print(sub_file.find("-"))

            sub_path = file_name + "/" + sub_file
            file_traverse(sub_path, index)
    else:
        return

file_traverse(path)