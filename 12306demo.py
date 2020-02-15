from urllib import request, parse
import ssl
import json
import base64

url = "https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&1580774057520&callback=jQuery191038044789367913723_1581522186971&_=1580774055548"

validate_code_resp = request.urlopen(url, timeout=10, context=ssl._create_unverified_context())

# 保存验证码
resp_str = validate_code_resp.read().decode("utf-8")
print(resp_str)
jquery_str = resp_str.split("(")[0].split("/")[2]
print("jquery_str: " + jquery_str)
start, end = resp_str.index("("), resp_str.rindex(")")
json_str = resp_str[start+1:end]
# print(str_resp)
# print(type(str_resp))

result = json.loads(json_str, encoding="utf-8")
# print(result["result_message"])
# print(base64.b64decode(result["image"]))

base64_img = base64.b64decode(result["image"])
# print(type(base64_img))

with open("yzm.jpg", "wb") as f:
    f.write(base64_img)

# print(validate_code_resp.getheader("set-cookie"))
cookies = validate_code_resp.getheader("set-cookie").split(",")

cookie_result = []
for cookie in cookies:
    cookie_result.append(cookie.split(";")[0])

# print("cookie_result: %s" % cookie_result)

headers = {
    "cookie": cookie_result
}

check_url = "https://kyfw.12306.cn/passport/captcha/captcha-check"
answer = input("请输入验证码：")

data = {
    "callback": jquery_str,
    "answer": answer,
    "rand": "sjrand",
    "login_site": "E",
    "_": "1581522186976"
}
parameter = bytes(parse.urlencode(data), encoding="utf-8")
print("parameter: " + str(parameter))

final_url = check_url + "&" + parse.urlencode(data)
print(final_url)

# req = request.Request(final_url, headers=headers)
# resp = request.urlopen(req)
# print(resp.getcode())



