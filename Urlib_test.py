from urllib import request, parse
import json
import ssl

fuli_url = "https://www.977yt.com"

mp3_url = "http://mvoice.spriteapp.cn/voice/2017/0515/591969966204f.mp3"
pic_url = "https://mmslt1.com/tp/girl/MyGirl/B-048/01.jpg"

study_url = "https://study.163.com/mob/search/independent/v1"

# parameter = {
#     "keyword": "王顺子",
#     "orderType": "50",
#     "pageIndex": "1",
#     "pageSize": "20",
#     "priceType": "-1",
#     "searchType": "0"
# }
#
# data = parse.urlencode(parameter)
# response = request.urlopen(study_url, data=bytes(data, encoding="utf-8"))
# # print(response.getheader("content-type"))
# json_str = response.read().decode("utf-8")
# resp_dict = json.loads(json_str, encoding="utf-8")
# print(resp_dict["results"]["resultPagination"]["query"])


def image_download():

    header = {
        "Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
        "Referer": "https://www.579ytr.com/meinv/76380.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
    }

    for i in range(3):
        i += 1
        if i < 10:
            num = "0" + str(i)
        else:
            num = str(i)

        url = "https://mmslt1.com/tp/girl/MyGirl/B-048/" + num + ".jpg"
        print(url)
        result = request.Request(url, headers=header)
        resp = request.urlopen(result)

        # print(type(resp.read()))
        # print(resp.getcode())

        if resp.getcode() == 200:
            name = str(i) + ".jpg"
            with open(name, "wb") as f:
                f.write(resp.read())


def hub_image_download():
    url = "https://ci.phncdn.com/pics/albums/049/507/411/602287941/"

    header = {
        "Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
        "Referer": "https://cn.pornhub.com/album/49507411",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }

    # result = request.Request(url, headers=header)
    # resp = request.urlopen(result, context=ssl._create_default_https_context())

    new_url = "https://di.phncdn.com/pics/albums/049/507/411/602287881/(m=e-yaaGqaa)(mh=Yt6gwShw_pEAwXQN)original_602287881.jpg"
              # "https://di.phncdn.com/pics/albums/049/507/411/602287891/(m=e-yaaGqaa)(mh=S8lBwpdVWXjBVDQ2)original_602287891.jpg"
              # "https://ci.phncdn.com/pics/albums/049/507/411/602287901/(m=e-yaaGqaa)(mh=zBAWq1ZnseOTyF3B)original_602287901.jpg"
    resp = request.urlopen(new_url)
    # print(type(resp.read()))
    # print(resp.getcode())
    with open("ym.png", "wb") as f:
        f.write(resp.read())


def get_url_scheme():
    url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.7367307074501106"

    resp = request.urlopen(url, context=ssl._create_unverified_context())

    print(resp.getcode())
    # print(resp.read())

    with open("validation_code.jpg", "wb") as f:
        f.write(resp.read())


get_url_scheme()



# result = request.Request(pic_url, headers=header)
# resp = request.urlopen(result)
#
# # print(resp.read())
# print(resp.getcode())
#
# if resp.getcode() == 200:
#     with open("mm.mp4", "wb") as f:
#         f.write(resp.read())
