import os

# dir_path = input("请输入文件夹路径：")
# dir_path = "/Users/jackie/Downloads/小鸟酱/小鸟酱 小草莓系列系列003-四套210P4V 果醬JK 聖誕小果醬 黑絲OL 藍白兔子比基尼"
dir_path = "/Users/jackie/Downloads/小鸟酱"

if not os.path.exists(dir_path):
    print("文件夹不存在")
    exit()


def file_rename(old_name, prefix):
    try:
        if os.path.exists(old_name):
            path = old_name.rfind("/")
            old = old_name.split("/")[-1]
            new_name = old_name[0:path+1] + prefix + "_" + old
            # print(old_name)
            # print(old_name[0:path+1])
            print(new_name)
            os.rename(old_name, new_name)
        else:
            print("old file not exist")
    except:
        print("fail: " + old_name)


def file_traversal(dir_path, index=0):
    index += 1
    if os.path.isdir(dir_path):
        for file in os.listdir(dir_path):
            # print("--" * index + dir_path + "/" + dir)
            dir_name = dir_path.split("/")[-1]
            # print(file)

            new_dir = dir_path + "/" + file
            file_traversal(new_dir, index=index)
    else:
        # print(dir_path)
        dir_name = dir_path.split("/")[-2]
        # print(file_name)
        # print(dir_name)
        # file_rename(dir_path, dir_name)

file_traversal(dir_path)