import requests

ak = "PmkYQbXLGxqHnQvRktDZCGMSHGOil2Yx"

def ride_indication(address, shop_list):

    final_list = []
    for (index, good) in enumerate(shop_list):

        shop = {}
        shop["title"] = good["title"]
        shop["address"] = good["address"]
        shop["latitude"] = good["latitude"]
        shop["longitude"] = good["longitude"]

        final_list.append(shop)
        print(index, good["title"], good["address"])

    orig_lat = str("%.6f" % float(address[0]))
    orig_lng = str("%.6f" % float(address[1]))

    # print(orig_lat, orig_lng)

    index = int(input("请输入选择的序号："))

    shop = final_list[index]
    des_lat = shop["latitude"]
    des_lng = shop["longitude"]

    ride_url = "http://api.map.baidu.com/direction/v2/riding?origin={},{}&destination={},{}&ak={}".format(orig_lat, orig_lng, des_lat, des_lng, ak)
    route_resp = requests.get(ride_url)
    # print(route_resp.json()["result"]["routes"]["steps"])

    result = route_resp.json()["result"]
    step_list = result["routes"][0]["steps"]

    for step in step_list:
        print(step["instructions"])

def meituan_get(key, address):
    print(address)
    get_header = {
        "uuid": "5DBAEC411BBD1E5C20EE784F5827EDA5B8E62FB5197A319B67812B49E6634DE0",
        "myLng": address[0],
        "utm_medium": "iphone",
        "myLat": address[1],
        "open_id": "oJVP50OIunB7-0GeCAihfS71QT5g",
        "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/7.0.10(0x17000a21) NetType/WIFI Language/zh_CN"
    }

    get_params = {
        "limit": "15",
        "mypos": "{},{}".format(address[0], address[1]),
        "cityId": "278",
        "q": key
    }

    # get
    get_url = "https://apimobile.meituan.com/group/v4/poi/pcsearch/278"
    get_resp = requests.get(get_url, params=get_params, headers=get_header, verify=False)
    result_list = get_resp.json()["data"]["searchResult"]

    ride_indication(address, result_list)


def meituan_post():
    post_params = {
        "wm_dtype": "iPhone 8 Plus (GSM+CDMA)<iPhone10,2>",
        "wm_uuid": "1122100804401172552",
        "wm_longitude": "110260609",
        "wm_latitude": "21375185",
        "wm_visitid": "223e025a-0d62-4483-802b-2d7886a9b63c",
        "wm_appversion": "5.2.1",
        "req_time": "1581776426207",
        "keyword": "烧烤",
        "sort_type": "0",
        "page_index": "0",
        "query_type": "1",
        "sub_category_type": "0",
        "category_type": "0"
    }

    post_header = {
        "Host": "wx.waimai.meituan.com",
        "uuid": "1122100804401172552",
        "Referer": "https://servicewechat.com/wx2c348cf579062e56/239/page-frame.html",
        "wm-ctype": "wxapp",
        "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/7.0.10(0x17000a21) NetType/WIFI Language/zh_CN"
    }

    # post
    post_url = "https://wx.waimai.meituan.com/weapp/v2/search/v9/poi"
    post_resp = requests.post(post_url, data=post_params, headers=post_header, verify=False)

    print(post_resp.status_code)
    print(post_resp.json())


def get_address_and_key():
    key = input("请输入要搜索的关键字：")
    address = input("请输入要搜索地点：")

    baidu_map_url = "http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak={}".format(address, ak)
    resp = requests.get(baidu_map_url)
    result = resp.json()["result"]
    print(result["location"]["lng"], result["location"]["lat"])
    lng = str(result["location"]["lng"])
    lat = str(result["location"]["lat"])
    location = (lat, lng)

    meituan_get(key, location)

get_address_and_key()