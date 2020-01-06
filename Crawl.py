import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#
# response = requests.get(link, headers=headers)
# # print(response.text)
#
# soup = BeautifulSoup(response.text, "lxml")
# title = soup.find("div", class_="col-md-8").article.text
#
# with open('title.txt', "a+") as f:
#     f.write(title)
#     f.close()
#
# print(title)

base_url = "https://www.952bqz.com/index/home.html"
video_url = "https://www.952bqz.com/shipin/list-国产精品.html"
# porn_link = "shipin"

response = requests.get(video_url)
response.encoding = 'utf8'
# print(response.status_code)
# print(response.encoding)
# print(response.text)


soup = BeautifulSoup(response.text, "lxml")
a_lable_list = soup.find_all("a")
# print(a_lable_list)


for label in a_lable_list:
    # with open('title.txt', "a") as f:
    #     f.write(str(a_lable_list))
    #     f.close()
    print(label['href'])

