import os
import shutil
import sys

# path = "/Users/jj/Desktop/book/"
# path = "/Users/jackie/Downloads/周杰伦全部专辑-无损音质版"
# path = input("请输入文件夹路径: ")
# path = "/Users/jackie/Downloads/new/徐vv"
path = "/Users/jackie/Music/网易云音乐"
#
# if not os.path.exists(path):
#     exit()


def file_rename(old_name, new_name, index=0):
    print("file_rename")
    if os.path.exists(old_name):
        if "." in old_name:
            suffix = old_name.split('.')[-1]
            # print(suffix)
            current_name = "%s %s.%s" % (new_name, index, suffix)
            print("current_name: ", current_name)

            path = old_name.rfind("/") + 1
            new_path = old_name[0:path] + current_name

            print("old_name: ", old_name)
            print("new_path: ", new_path)
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


def file_filter_remove(path, file_name, filter_key):
    suffix = file_name.split(".")[-1]
    full_path = path+ "/" + file_name

    if suffix == filter_key:
        os.remove(full_path)


def folder_remove(folder_name, filter_key):
    if filter_key in folder_name:
        print(folder_name)
        os.rmdir(folder_name)


def file_move(path, default_dir):

    if not os.path.exists(default_dir):
        os.makedirs(default_dir)

    shutil.move(path, default_dir)


def file_filter_move(dir, path, sub_path, file_name, target_suffix):
    dir_path = os.path.join(path, dir)
    if not os.path.exists():
        os.mkdir(dir_path)

    file_suffix = file_name.split(".")[-1]
    if file_suffix == target_suffix:
        print(file_name)
        file_move(sub_path, dir_path)


def file_collection():
    path = input("请输入文件夹路径, 留空为当前文件夹路径：")
    new_dir = str(input("请输入新文件夹名称："))

    if not os.path.exists(path + "/" + new_dir):
        os.mkdir(path + "/" + new_dir)

    # exit(33)
    total_list = os.listdir(path)
    # print("total_list: ", total_list)
    dir_list = []
    for dir in total_list:
        # print(dir)
        # print(os.path.isdir(path + "/" + dir))
        if os.path.isdir(path + "/" + dir) and dir[0] != ".":
            dir_list.append(dir)
    print(dir_list)

    for dir in dir_list:
        dir_path = path + "/" +dir
        for file in os.listdir(dir_path):
            try:
                ori = dir_path + "/" + file
                if os.path.isfile(ori):
                    des = path + "/" + new_dir
                    print(ori)
                    print(des)
                    # print("-" * 50)
                    # shutil.move(ori, des)
            except Exception as e:
                print("files move error: ", e)


dir_name = ""
def file_traverse(file_name, index=0):
    # 重命名是需注释掉
    index += 1

    # 重命名开启计数
    # count = index
    if os.path.isdir(file_name):

        for sub_file in os.listdir(file_name):

            # print(index * "-" + sub_file)
            sub_path = os.path.join(file_name, sub_file)

            # 遍历文件夹内文件并记录
            # with open("python教程文档.txt", "a+") as f:
            #     f.write(sub_file+'\n')

            # 文件过滤
            # file_filter(file_name, sub_file, "txt")

            # 重命名
            # count += 1
            # file_rename(sub_path, sub_file, count)

            # 名称拼接
            # file_name_append(sub_path, sub_file, dir_name)

            # 网易云歌曲移动文件夹
            # singer = "林俊杰"
            # if singer in sub_file:
            #     print(sub_file)
            #     default_dir = "/Users/jackie/Downloads/" + singer
            #     file_move(sub_path, default_dir)

            # 提取指定后缀文件到文件夹
            # file_filter_move("ncm_dir", path, sub_path, sub_file, "ncm")

            # 删除包含指定字符的文件夹
            # folder_remove(sub_path, "dir")

            file_traverse(sub_path, index)


file_traverse(path)
# file_collection()

# if __name__ == '__main__':
#     print(sys.argv[0])
#     print(sys.argv[1])