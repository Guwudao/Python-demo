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

    url1 = "https://www.meitulu.com/item/20818.html"

    # resp.encoding = "utf-8"
    # print(resp.content)

    for i in range(96):
        # d_url = f"https://mtl.gzhuibei.com/images/img/20818/{i+1}.jpg"
        # d_url = f"https://mtl.gzhuibei.com/images/img/20831/{i+1}.jpg"
        # d_url = f"https://mtl.gzhuibei.com/images/img/20828/{i+1}.jpg"
        # d_url = f"https://mtl.gzhuibei.com/images/img/20811/{i+1}.jpg"
        # d_url = f"https://mtl.gzhuibei.com/images/img/20791/{i+1}.jpg"
        d_url = f"https://mtl.gzhuibei.com/images/img/20779/{i+1}.jpg"

        prefix = "杨晨晨sugar_"
        suffix = "剧情写真"
        name = prefix + suffix + str(i+1) + ".jpg"
        resp = requests.get(d_url)

        dir_name = prefix + suffix

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            # os.chdir(dir_name)


        with open(f"./{dir_name}/{name}", "wb") as f :
            f.write(resp.content)


def bs_demo():
    url = "https://www.meitulu.com/t/sugar-xiaotianxincc/"

    resp = requests.get(url)
    resp.encoding = "utf-8"
    bs = BeautifulSoup(resp.text, "html.parser")
    # print(bs.title)

    a_list = list(bs.find_all("a"))
    title_list, url_list = [], []

    for a in a_list:
        content = a.get_text()
        if "杨晨晨" in content and len(content) > 3:
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

    # print(title_list)
    # print(url_list)
    secondary_page(title_list, url_list, count_list)


def secondary_page(title_list, url_list, count_list):

    for title, url, count in zip(title_list, url_list, count_list):
        resp = requests.get(url)
        resp.encoding = "utf-8"
        bs = BeautifulSoup(resp.text, "html.parser")
        center = bs.find_all("center")

        child = center[0].children

        temp_url = ""
        for c in child:
            temp_url = c.get("src")

        # print(temp_url)
        index = temp_url.rfind("/")
        base_url = temp_url[0:index + 1]
        print(base_url)

        print(title)
        name =title.split(" ")[-1]
        print(name)
        print("-" * 50)

        # download_bot(name, base_url, count)


def download_bot(title, base_url, count):
    if not os.path.exists(title):
        os.makedirs(f"./YYY/{title}")




# douban_movie()
# juhe_news()
# juhe_cp()
# image_get()

bs_demo()