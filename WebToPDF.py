import pdfkit


pdfkit.from_file("pdf_target.html", "chrome.pdf")
# pdfkit.from_url("https://zhuanlan.zhihu.com/p/32825491", "chrome.pdf")

from datetime import datetime
import threading
import time

# start = time.time()
# print(start)
# time.sleep(5)
# # print(time.localtime(time.time()))
# end = time.time()
#
# interval = end - start
# hour, min, sec = 0, 0, 0
# if interval > 3600:
#     hour = interval // 3600
# elif interval > 60:
#     min = interval // 60
# elif interval > 1:
#     sec = interval // 1
#
# print("时间：{} : {} : {}".format(hour, min, sec))

# print(datetime.now().strftime("%H:%M:%S"))


# def receive_msg():
#     start_time_monitor()
#
#
# def execute():
#     print("reminder")
#     timer = threading.Timer(5, execute)
#     timer.start()
#     print(datetime.now().strftime("%H:%M:%S"))
#     end = time.time()
#     interval = end - start
#
#     if interval > 30:
#         timer.cancel()
#
#
# def start_time_monitor():
#     timer = threading.Timer(10, execute)
#     timer.start()
#
#
# # receive_msg()
# timer = threading.Timer(1, execute)
# timer.start()
# start = time.time()

import itertools

char = ["a", "b", "c", "d", "e", "f"]
print(list(itertools.combinations(char, r=4)))