from urllib import request, parse

fuli_url = "https://www.977yt.com"

mp3_url = "http://mvoice.spriteapp.cn/voice/2017/0515/591969966204f.mp3"
pic_url = "https://mmslt1.com/tp/girl/MyGirl/B-048/01.jpg"

study_url = "https://study.163.com/mob/search/independent/v1"

parameter = {
    "keyword": "王顺子",
    "orderType": "50",
    "pageIndex": "1",
    "pageSize": "20",
    "priceType": "-1",
    "searchType": "0"
}

data = parse.urlencode(parameter)
print(data)
response = request.urlopen(study_url, data=bytes(data, encoding="utf-8"))
print(response.getheader("content-type"))
print(response.read().decode("utf-8"))


def image_download():

    header = {
        "Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
        "Referer": "https://www.579ytr.com/meinv/76380.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
    }

    for i in range(34):
        i += 1
        if i < 10:
            num = "0" + str(i)
        else:
            num = str(i)

        url = "https://mmslt1.com/tp/girl/MyGirl/B-048/" + num + ".jpg"
        print(url)
        result = request.Request(url, headers=header)
        resp = request.urlopen(result)

        # print(resp.read())
        # print(resp.getcode())

        if resp.getcode() == 200:
            name = str(i) + ".jpg"
            with open(name, "wb") as f:
                f.write(resp.read())


# result = request.Request(pic_url, headers=header)
# resp = request.urlopen(result)
#
# # print(resp.read())
# print(resp.getcode())
#
# if resp.getcode() == 200:
#     with open("mm.mp4", "wb") as f:
#         f.write(resp.read())


