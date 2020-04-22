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
res8 = re.findall("[^0-9]", str)
res9 = re.findall("[^a-z]", str)
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

res13 = re.findall(r"\b(?:ba)+", str)
# print(res13)

res14 = re.findall(r"\b[a-z]+\d*\b", str)
print(res14)

res15 = re.findall(r"[a-z]+\d+", str)
print(res15)

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