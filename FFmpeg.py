import os
import re
import subprocess

video_list = []


def get_all_videos(file_path):

    for file_name in os.listdir(file_path):
        # print(file_name)
        new_path = os.path.join(file_path, file_name)
        if os.path.isdir(new_path):
            get_all_videos(new_path)

        elif os.path.isfile(new_path):
            result = re.match(r".+\.(mp4|mkv)$", new_path)
            if result:
                video_list.append(new_path)

        else:
            print("It's not a directory or a file.")

    print(video_list)


def file_processing(file_list):
    print("start----------------")
    code_pre = "ffmpeg -i "
    code_mid = " -b:v 2000k "

    for file_name in file_list:
        old_name = file_name.split(".")
        new_name = old_name[0] + "_new.mkv"
        # print(new_name)

        command = code_pre + file_name + code_mid + new_name
        test_name = os.path.basename(file_name).split('.')
        try:
            retcode = subprocess.call(command, shell=True)
            if retcode == 0:
                print(test_name[0], "success----------")
            else:
                print(test_name[0], "is failed--------")
        except Exception as e:
            print("Error:", e)
        # print(command)

    print("---------------End all-----------------")


class VideoOperation:

    def video_compress(self, video_path, output_path):
        pass


if __name__ == '__main__':
    path = input("请输入文件夹路径: ")
    if not os.path.exists(path):
        print("文件路径有误")
        exit()

    get_all_videos(path)
    file_processing(video_list)
