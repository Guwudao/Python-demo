import requests


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

# juhe_news()

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

juhe_cp()