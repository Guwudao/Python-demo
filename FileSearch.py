import os
# import shutil

path = "/Users/jj/Desktop/book/"

if not os.path.exists(path):
    exit()

# os.chdir(path)
# file_list = os.listdir("./")
# print(file_list)

# print(os.getcwd())
# os.rename('1 (1).jpg', 'new.jpg')


def file_rename(old_name, new_name, index=0):
    if os.path.exists(old_name):
        suffix = old_name.split('.')[-1]

        print(old_name)
        name = "%s %s.%s" % (new_name, index, suffix)
        print(name)
        os.rename(old_name, name)


def file_traverse(file_name, index=0):
    index += 1

    if os.path.isdir(file_name):
        for sub_file in os.listdir(file_name):
            print(index * "-" + sub_file)
            # num = filter(str.isdigit(), sub_file)
            # print(num)

            # 重命名
            # index += 1
            # file_rename(sub_file, "龙珠", index)

            sub_path = file_name + "/" + sub_file
            file_traverse(sub_path, index)
    else:
        # print(file_name)
        return


file_traverse(path)
