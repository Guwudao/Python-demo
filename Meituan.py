import requests

get_header = {
    "uuid": "5DBAEC411BBD1E5C20EE784F5827EDA5B8E62FB5197A319B67812B49E6634DE0",
    "myLng": "21.377765655517578",
    "utm_medium": "iphone",
    "myLat": "110.25626373291016",
    "open_id": "oJVP50OIunB7-0GeCAihfS71QT5g",
    "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/7.0.10(0x17000a21) NetType/WIFI Language/zh_CN"
}

get_params = {
    "limit": "15",
    "mypos": "21.377765655517578,110.25626373291016",
    "cityId": "278",
    "q": "烧烤"
}

# get
get_url = "https://apimobile.meituan.com/group/v4/poi/pcsearch/278"
# get_resp = requests.get(get_url, params=get_params, headers=get_header, verify=False)


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
# try:
post_resp = requests.post(post_url, data=post_params, headers=post_header, verify=False)
# except requests.exceptions.ConnectTimeout as re:
#     print("error: " + re)

print(post_resp.status_code)
print(post_resp.json())