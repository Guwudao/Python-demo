import os
import shutil

path = "/Users/jackie/Downloads/Python阶段资料/04-异常处理"

if not os.path.exists(path):
    exit()

os.chdir(path)
file_list = os.listdir("./")
# print(file_list)

print(os.getcwd())

# for file_name in file_list:
    # print("-" + file_name)
    # if os.path.isdir(file_name):
    #     for sub_files in os.listdir(file_name):
    #         print("--" + sub_files)


def file_traverse(file_name, index=0):
    index += 1
    if os.path.isdir(file_name):
        for sub_file in os.listdir(file_name):

            print(index * "-" + sub_file)
            file_traverse(sub_file, index)
    else:
        return

file_traverse(path)