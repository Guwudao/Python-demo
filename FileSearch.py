import os
# import shutil


# path = "/Users/jj/Desktop/book/"
path = "/Users/jackie/Downloads/龙珠"
# path = input("请输入文件夹路径: ")
# path = "/Users/jackie/Downloads/小鸟酱"


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


def file_fliter(path, file_name):
    suffix = file_name.split(".")[-1]
    full_path = path+ "/" + file_name

    if suffix == "xltd":
        os.remove(full_path)


def file_traverse(file_name, index=0):
    # index += 1
    if os.path.isdir(file_name):
        for sub_file in os.listdir(file_name):

            # print(index * "-" + sub_file)
            # num = filter(str.isdigit(), sub_file)
            # print(num)

            # 重命名
            index += 1
            # file_fliter(file_name, sub_file)
            sub_path = file_name + "/" + sub_file
            # file_rename(sub_path, "龙珠", index)
            file_traverse(sub_path, index)
    else:
        suffix = file_name.split('.')[-1]
        # if suffix == "xltd":
        #     print(file_name)
        #     os.remove(file_name)
        return


file_traverse(path)
