import re

str = "about123ba123ba123ba123b"
weather = "全额奥多天气"

# res = re.findall(r"a(.+)b", str)
# res1 = re.findall(r"a(.+?)b", str)
# res2 = re.findall(r"a(.*)b", str)
# res3 = re.findall(r".(?=[^.]*$)", weather)

# print(res)
# print(res1)
# print(res2)

# res4 = re.findall("\d+", str)
# print(res4)

# res5 = re.search("\d+", str)
# print(res5)
# print(type(res5))
# print(res5.group())

# res6 = re.split("\d+", str)
# print(res6)
# res7 = re.split("(\d+)", str)
# print(res7)
#
# res8 = re.findall("[^0-9]", str)
# res9 = re.findall("[^a-z]", str)
# print(res8)
# print(res9)

str = "about123 baba123 ba ab1 123ba123b 12ba1"
# res11 = re.findall(r"\bba\b", str)
# print(res11)
#
# res10 = re.findall(r"[a-z]+\d+", str)
# print(res10)
#
# res12 = re.findall(r"\b[a-z]+\d+?\b", str)
# print(res12)

# res13 = re.findall(r"\b(?:ba)+", str)
# # print(res13)
#
# res14 = re.findall(r"\b[a-z]+\d*\b", str)
# print(res14)
#
# res15 = re.findall(r"[a-z]+\d+", str)
# print(res15)

# str = "a, b,;,;c  d  ;, e"
# res16 = re.split(r"[\s\,\;]+", str)
# print(res16)

# str = "010-12345231"
# res17 = re.match(r"\d{3}\-\d{3,8}", str)
# print(res17)
# if res17:
#     print("ok")
# else:
#     print("no")

# res18 = re.match(r"(\d{3})-(\d{3,8})", str)
# print(res18.group(0))
# print(res18.group(1))
# print(res18.group(2))

# str =r"/* part 1 */ code /* part 2 */"
# res19 = re.findall(r"/\*.*?\*/", str)
# print(res19)
#
# res20 = re.findall(r"(?<=/\*).+?(?=\*)", str)
# print(res20)

str = r"aaa111aaa , bbb222 , 333ccc"
res21 = re.findall(f"[a-z]+(\d+)[a-z]+", str)
print(res21)

# s = "123 10e3 20e4e4 30ee5"
# r = re.findall(r"\d+[eE]?\d*", s)
# print(r)


def foo(*args, **kwargs):
    for arg in args:
        print("in the args: ", arg)

    for k,v in kwargs.items():
        print("key = {}, value = {}".format(k, v))


tuple = (1, 2, 3, 4)
list = [11, 22, 33, 44]
dic = {"a":1, "b":2, "c":3}

# foo(1, 2, 33, 44, e=tuple, f=list, **dic)
# foo(tuple, list, dic)
# foo(tuple, *list, **dic)
# foo(1, 2, *list)

print([x*11 for x in range(10)])


def check(func):
    def inner(*args, **kwargs):
        print("check")
        res = func(*args, **kwargs)
        return res
    return inner


@check
def sendMsg():
    print("send msg")


@check
def ss(a):
    print(a)
    return a

@check
def sss(a, b):
    print(a + b)

# sendMsg()

res1 = ss(10)
res2 = sss(10, 20)

print(res1, res2)