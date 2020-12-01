import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor

video_list = []


def get_all_videos(file_path):

    for file_name in os.listdir(file_path):
        # print(file_name)
        new_path = os.path.join(file_path, file_name)
        if os.path.isdir(new_path):
            get_all_videos(new_path)

        elif os.path.isfile(new_path):
            result = re.match(r".+\.(mp4|mkv|avi|flv)$", new_path)
            if result:
                video_list.append(new_path)

        else:
            print("It's not a directory or a file.")

    print(video_list)

def file_converse(info):
    print(f"================ {info[0]} begin ================")
    try:
        retcode = subprocess.call(info[1], shell=True)
        if retcode == 0:
            print(info[0], "success----------")
        else:
            print(info[0], "is failed--------")
    except Exception as e:
        print("Error:", e)


def file_processing(file_list):
    code_pre = "ffmpeg -i "
    # code_mid = " -b:v 800k "
    code_mid = " "


    with ThreadPoolExecutor(max_workers=1) as pool:
        for file_name in file_list:
            try:
                old_name = "_".join(file_name.split(".")[:-1])
                new_name = old_name + "_new.mp4"
                print("old_name: ", old_name)
                print("new_name: ", new_name)

                command = code_pre + file_name + code_mid + new_name
                test_name = os.path.basename(file_name).split('.')
                print("command: " + command)

                pool.map(file_converse, [(test_name[0], command)])
            except Exception as e:
                print("convert error: ", e)
        # print(command)

    print("---------------End all-----------------")


if __name__ == '__main__':
    path = str(input("请输入文件夹路径: "))
    if not os.path.exists(path):
        print("文件路径有误")
        exit()

    get_all_videos(path)
    file_processing(video_list)
