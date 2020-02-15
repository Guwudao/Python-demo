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


study163()