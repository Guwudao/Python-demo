import os
import shutil


# path = "/Users/jj/Desktop/book/"
# path = "/Users/jackie/Downloads/周杰伦全部专辑-无损音质版"
# path = input("请输入文件夹路径: ")
path = "/Users/jackie/Downloads/CC"
# path = "/Users/jackie/Music/网易云音乐"

if not os.path.exists(path):
    exit()


def file_rename(old_name, new_name, index=0):
    if os.path.exists(old_name):
        if "." in old_name:
            suffix = old_name.split('.')[-1]
            # print(suffix)
            current_name = "%s %s.%s" % (new_name, index, suffix)
            # print(current_name)

            path = old_name.rfind("/") + 1
            new_path = old_name[0:path] + current_name

            # print(old_name)
            # print(new_path)
            os.rename(old_name, new_path)
        else:
            # os.rename(old_name, new_name)
            print("pass")
    else:
        print("fail")


def file_name_append(path, old_name, prefix):
    if not os.path.isdir(path):
        print(path)
        new_name = prefix + " - " + old_name
        index = path.rfind("/") + 1
        final = path[0:index] + new_name
        print(final)
        print("-" * 30)

        os.rename(path, final)


def file_filter(path, file_name, filter_key):
    suffix = file_name.split(".")[-1]
    full_path = path+ "/" + file_name

    if suffix == filter_key:
        os.remove(full_path)


def file_move(path, default_dir):
    if not os.path.exists(default_dir):
        os.makedirs(default_dir)

    shutil.move(path, default_dir)


dir_name = ""
def file_traverse(file_name, index=0):
    index += 1

    # 重命名计数
    # count = index
    if os.path.isdir(file_name):

        for sub_file in os.listdir(file_name):

            print(index * "-" + sub_file)
            sub_path = file_name + "/" + sub_file

            # 遍历文件夹内文件并记录
            # with open("python教程文档.txt", "a+") as f:
            #     f.write(sub_file+'\n')

            # 文件过滤
            # file_filter(file_name, sub_file, "xltd")

            # 重命名
            # count += 1
            # file_rename(sub_path, "YCC", count)

            # 名称拼接
            # file_name_append(sub_path, sub_file, dir_name)

            # 移动文件夹
            # singer = "陈奕迅"
            # if singer in sub_file:
            #     print(sub_file)
            #     default_dir = "/Users/jackie/Downloads/" + singer
            #     file_move(sub_path, default_dir)
            #
            # file_traverse(sub_path, index)


file_traverse(path)
