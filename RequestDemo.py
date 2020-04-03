import requests
import json
import ssl

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


douban_movie()
# juhe_news()
# juhe_cp()
