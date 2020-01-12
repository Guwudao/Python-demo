import itchat
from itchat.content import *
import requests
from lxml import etree
from pyecharts.charts import Bar
import re

# itchat.send_msg("this is a test message", toUserName="filehelper")

url = "http://openapi.tuling123.com/openapi/api/v2"

signal_thread = "0e4dc4f3608b4da38dbbac4c746b6428"
not_robot_key = "7714085bddd24e7aa77b071d8eaec5db"


class Person:

    def __init__(self, name, age, height, weight, gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

        try:
            if isinstance(age, str):
                self.age = int(age)

            if isinstance(height, str):
                self.height = float(height)
                if self.height > 10:
                    self.height = self.height / 100

            if isinstance(weight, str):
                self.weight = float(weight)

            if gender in ("男", "女"):
                self.gender = 1 if gender == "男" else 0

        except Exception:
            raise Exception("请输入正确格式")

    @property
    def get_body_fat(self):
        bmi = self.weight / (self.height * self.height)
        body_fat = (1.2 * bmi + 0.23 * self.age - 0.54 - 10.8 * self.gender) / 100

        body_fat_scop = ((0.25, 0.28), (0.15, 0.18))
        min_fat, max_fat = body_fat_scop[self.gender]

        result = "正常"
        if body_fat < min_fat:
            result = "偏瘦"
        elif body_fat > max_fat:
            result = "偏胖"
        print("BMI = %f" % bmi, "体脂率 = %f" % body_fat)

        result_str = "{} 您好，您的体脂率是{}, 正常体脂率的范围是{} - {}, 您的体型属于{}".format(self.name, body_fat, min_fat, max_fat, result)
        return result_str


itchat.auto_login(hotReload=True)

print(itchat.get_friends()[0]["City"])

friends = itchat.get_friends()
sex_title = ["未知", "男", "女"]
sex_count = [0, 0, 0]
cities, count = [], []

for friend in friends:
    sex = friend["Sex"]
    sex_count[sex] += 1
    # print(friend["City"])

    city = friend["City"]
    if city not in cities:
        cities.append(city)

length = len(cities)

for i in range(length):
    count.append(0)

for friend in friends:
    for i in range(length):
        if friend["City"] == cities[i]:
            count[i] += 1

new_list = [(i, j) for (i, j) in zip(cities, count) if j >= 4]
new_list.sort(key=lambda x: x[1], reverse=True)
print(new_list)

final_city, final_count = [], []

for i, j in new_list:
    if len(i):
        final_city.append(i)
        final_count.append(j)

print(final_city, final_count)

bar_sex = Bar()
bar_sex.add_xaxis(sex_title)
bar_sex.add_yaxis("微信好友性别数据统计", sex_count)
bar_sex.render("sex.html")

bar_city = Bar()
bar_city.add_xaxis(final_city)
bar_city.add_yaxis("微信好友地区数据统计", final_count)
bar_city.render("city.html")


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):

    if msg["User"]["NickName"] == "CTT" or msg["User"]["NickName"] == "JJ1" or msg["User"]["NickName"] == "fat fish":
        # print("自己人，别乱来")
        print("{} ---> {}".format(msg["User"]["NickName"], msg))
        return

    print(msg)

    if not msg["Content"]:
        return "我是个么得感情的复读机 -- 但我并不打算复读这个"
    else:
        msg.download(msg.fileName)
        type_symbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        itchat.send_msg("看我反弹大法！！！", toUserName=msg["FromUserName"])
        return '@%s@%s' % (type_symbol, msg.fileName)


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    # if msg.user["NickName"] == "CTT" or msg.user["NickName"] == "JJ1" or msg.user["NickName"] == "fat fish":
    #     # print("自己人，别乱来")
    #     print("{} ---> {}".format(msg["User"]["NickName"], msg.text))
    #     return
    myself = itchat.get_friends()[0]["UserName"]
    if myself == msg["ToUserName"]:
        if isinstance(msg.text, str):
            content = TuringBot.automatic_reply(msg.text)
            print("机器人：%s" % content)
            if content == "请求次数超限制!":
                return "我变成个么得感情的复读机了:\n {}".format(msg.text)
            else:
                itchat.send_msg(content, toUserName=msg["FromUserName"])

            # print(msg["User"]["NickName"] == "JJ")
            #
            # result = re.match(r"(.*)[，,](.*)[，,](.*)[，,](.*)[，,](.*)", content)
            #
            # if result:
            #     try:
            #         p = Person(*result.groups())
            #     except Exception:
            #         return "我是个么得感情的复读机 -- 但我并不打算复读这个"
            #     # print(p.get_body_fat)
            #     itchat.send_msg(p.get_body_fat, toUserName=msg["FromUserName"])
            # else:
            #     print(msg)
            #     return "我是个么得感情的复读机:\n {}".format(msg.text)

        elif msg.type == "Picture":

            print(msg["Content"])
            print("--"*40)
            html_lxml = etree.HTML(msg["Content"])
            cdnurl = html_lxml.xpath("//emoji/@cdnurl")
            print(cdnurl)

            itchat.send_msg(cdnurl[0], toUserName=msg["FromUserName"])
            return "我是个么得感情的复读机 -- 但我并不打算复读这个"
        else:
            return "我是个么得感情的复读机:\n {}".format(msg)


class TuringBot:

    url = "http://openapi.tuling123.com/openapi/api/v2"

    signal_thread = "0e4dc4f3608b4da38dbbac4c746b6428"
    not_robot_key = "7714085bddd24e7aa77b071d8eaec5db"

    @classmethod
    def automatic_reply(cls, text):

        parameter_json = {
                            "reqType": 0,
                            "perception": {
                                "inputText": {
                                    "text": text
                                }
                            },
                            "userInfo": {
                                "apiKey": cls.not_robot_key,
                                "userId": "single"
                            }
                        }

        response = requests.post(cls.url, json=parameter_json)
        return response.json()["results"][0]["values"]["text"]


itchat.run()
