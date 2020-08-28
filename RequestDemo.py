import requests
import json
import ssl
import os
import re
from bs4 import BeautifulSoup

def study163():
    study_url = "https://study.163.com/mob/search/independent/v1"

    parameter = {
        "keyword": "王顺子",
        "orderType": "50",
        "pageIndex": "1",
        "pageSize": "20",
        "priceType": "-1",
        "searchType": "0"
    }

    resp = requests.request("post", study_url, data=parameter, verify=False)
    print(resp.ok)
    print(resp.status_code)
    # print(resp.json())
    print(resp.text)


# study163()


def juhe_news():
    url = "http://v.juhe.cn/toutiao/index"
    params = {
        "key": "b2d83e113c1e52d875122ad241ceabd3"
    }

    resp = requests.get(url, params=params)
    print(resp.status_code)
    data_list = resp.json()["result"]["data"]
    for data in data_list:
        print(data)


def juhe_cp():
    name = input("请输入菜名: ")
    url = "http://apis.juhe.cn/cook/query.php"
    params = {
        "menu": name,
        "key": "3a61638fad5dbab9c786216420b00b4c"
    }

    resp = requests.get(url, params=params)
    print(resp.status_code)
    print(resp.json())


def douban_movie():
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"

    headers = {
        "Host": "movie.douban.com",
        "User - Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15",
    }
    resp = requests.get(url, headers=headers, verify=False)

    print(resp.status_code)
    print(resp.text)
    # print(json.loads(resp.text, encoding="utf-8"))
    print("----")


def image_get():
    url = "https://www.meitulu.com/t/sugar-xiaotianxincc/"

    for i in range(48):
        # d_url = f"https://mtl.gzhuibei.com/images/img/20779/{i+1}.jpg"
        # d_url = f"https://mtl.gzhuibei.com/images/img/10183/{i+1}.jpg"
        d_url = f"https://mtl.gzhuibei.com/images/img/8019/{i+1}.jpg"

        prefix = "菲儿_"
        suffix = "奶牛"
        name = prefix + suffix + str(i+1) + ".jpg"
        resp = requests.get(d_url)

        dir_name = prefix + suffix

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        with open(f"./{dir_name}/{name}", "wb") as f :
            f.write(resp.content)


def bs_demo():
    # url = "https://www.meitulu.com/t/sugar-xiaotianxincc/"
    url = "https://www.meitulu.com/t/ningmengc-lemon/2.html"

    resp = requests.get(url)
    resp.encoding = "utf-8"
    # print(resp.text)
    bs = BeautifulSoup(resp.text, "html.parser")
    # print(bs.title)

    print(bs.find_all("p")[0].find_all("a"))

    pa_list = []
    for p in bs.find_all("p"):
        pa_tag = p.find_all("a")
        # print(pa_tag)

        if len(pa_tag) > 0 and "[" in pa_tag[0].get_text() :
            pa_list.append(pa_tag[0].get("href"))

    print(len(pa_list))


    a_list = list(bs.find_all("a"))
    title_list, url_list = [], []
    # print(a_list)

    for a in a_list:
        content = a.get_text()
        # print(content)
        if ("妲己" in content) and len(content) > 3:
        #     print(content)
            title_list.append(content)
            url_list.append(a.get("href"))

        # print(a.get_text())
        # print(a.get("href"))

    p_list = list(bs.find_all("p"))
    # print(p_list)

    count_list = []
    for p in p_list:
        if "图片" in p.get_text():
            num = re.findall(r"\d+", p.get_text())
            count_list.append(num[0])

    title_list = list(set(title_list))
    title_list.remove("妲己_Toxic")

    # print(title_list)
    # print(len(title_list))

    # print(url_list)
    # print(len(url_list))
    # print(count_list)
    # print(len(count_list))

    if len(title_list) == len(pa_list) and len(title_list) == len(count_list):
        secondary_page(title_list, pa_list, count_list)
    else:
        print("数据不对等，已暂停")
        print(f"title_list: {len(title_list)}, pa_list: {len(pa_list)}, count_list: {len(count_list)}")
        return


def secondary_page(title_list, url_list, count_list):

    print(len(title_list))
    print(len(url_list))
    print(len(count_list))
    acc = 0
    for title, url, count in zip(title_list, url_list, count_list):
        resp = requests.get(url)
        resp.encoding = "utf-8"
        bs = BeautifulSoup(resp.text, "html.parser")
        center = bs.find_all("center")

        child = center[0].children

        temp_url = ""
        for c in child:
            temp_url = c.get("src")

        index = temp_url.rfind("/")
        base_url = temp_url[0:index + 1]
        # print(base_url)

        acc += 1
        name =title.split(" ")[-1] + str(acc)
        # print(name)

        download_bot(name, base_url, count)


def download_bot(title, base_url, count):
    if not os.path.exists(title):
        os.mkdir(title)

    print(count)
    for i in range(int(count)):
        print(i)
        url = base_url + str(i) + ".jpg"
        print(url)
        resp = requests.get(url)
        name = title + "_" + str(i) + ".jpg"

        print(name)

        with open(f"{title}/{name}", "wb") as f:
            f.write(resp.content)



# douban_movie()
# juhe_news()
# juhe_cp()
image_get()

# bs_demo()