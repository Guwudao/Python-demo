import os
from PIL import Image, ImageFilter, ImageOps

img = Image.open("IMG_9513.jpg")

def dodge(a, b, alpha):
    return min(int(a*255/(256 - b*alpha)), 255)

def draw(img, blur=25, alpha=1.0, save_name="name"):
    img1 = img.convert("L")
    img2 = img1.copy()
    img2 = ImageOps.invert(img2)

    for i in range(blur):
        img2 = img2.filter(ImageFilter.BLUR)

    width, height = img1.size
    for x in range(width):
        for y in range(height):
            a = img1.getpixel((x, y))
            b = img2.getpixel((x, y))
            img1.putpixel((x, y), dodge(a, b, alpha))

    # img1.show()
    img1.save(save_name)
    print("complete--------------", save_name.split("/")[-1])

draw(img, save_name="IMG_95131.jpg")

# for i in range(70):
#     i = i+1
#     file_name = f"./CC/cc {i}.jpg"
#     img = Image.open(file_name)
#     save_name = f"./CC/YCC_{i}.jpg"
#     draw(img, save_name=save_name)

# dir_path = input("请输入文件夹路径：")
# dir_path = "/Users/jackie/Downloads/小鸟酱/小鸟酱 小草莓系列系列003-四套210P4V 果醬JK 聖誕小果醬 黑絲OL 藍白兔子比基尼"
dir_path = "/Users/jackie/Downloads/小鸟酱"

if not os.path.exists(dir_path):
    print("文件夹不存在")
    exit()


def file_move(old_path):
    dir_name = old_path.split("/")[-2]
    print(dir_name)
    default_prefix = "/Users/jackie/Downloads/Compress/"

    if not os.path.exists(default_prefix + dir_name):
        os.makedirs(default_prefix + dir_name)


def get_file_size(file):
    size = os.path.getsize(file)
    return  size // 1024 #kb


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
        print(dir_path)
        dir_name = dir_path.split("/")[-2]
        # print(file_name)
        # print(dir_name)
        # file_rename(dir_path, dir_name)
        # size = get_file_size(dir_path)
        # print(str(size) + "kb")
        file_move(dir_path)

# file_traversal(dir_path)