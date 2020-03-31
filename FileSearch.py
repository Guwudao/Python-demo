import os
# import shutil


# path = "/Users/jj/Desktop/book/"
# path = "/Users/jackie/Downloads/龙珠"
path = input("请输入文件夹路径: ")
# path = "/Users/jackie/Downloads/Others"


if not os.path.exists(path):
    exit()


def file_rename(old_name, new_name, index=0):
    if os.path.exists(old_name):
        if "." in old_name:
            suffix = old_name.split('.')[-1]
            if 0 == index:
                print(suffix)
                current_name = "%s %s.%s" % (new_name, index, suffix)
                print(current_name)
            else:
                current_name = "%s.%s" % (new_name, suffix)

            os.rename(old_name, current_name)
        else:
            os.rename(old_name, new_name)


def file_fliter(path, file_name):
    suffix = file_name.split(".")[-1]
    full_path = path+ "/" + file_name

    if suffix == "xltd":
        os.remove(full_path)


def file_traverse(file_name, index=0):
    index += 1

    if os.path.isdir(file_name):
        for sub_file in os.listdir(file_name):

            # print(index * "-" + sub_file)
            # num = filter(str.isdigit(), sub_file)
            # print(num)

            # 重命名
            # index += 1
            # file_rename(sub_file, "龙珠", index)
            # file_fliter(file_name, sub_file)

            sub_path = file_name + "/" + sub_file
            file_traverse(sub_path, index)
    else:
        # suffix = file_name.split('.')[-1]
        # if suffix == "xltd":
        #     print(file_name)
        #     os.remove(file_name)
        return


file_traverse(path)
