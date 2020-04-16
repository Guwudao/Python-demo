import json
from jsonpath import jsonpath

class Phone():
    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price


test_json = {
                "age": 18,
                "dog": {
                    "age": 2,
                    "child": None,
                    "color": "黑色",
                    "isVIP": True,
                    "name": "煤球"
                },
                "name": "sz",
                "phone": Phone("XSMax", 9999)
            }


class Phone_parse(json.JSONEncoder):
    def default(self, o):
        return {o.name: o.name, o.price: o.price}

def parse(obj):
    return [obj.name, obj.price]

# print(json.dumps(test_json, ensure_ascii=False, indent=4, allow_nan=False, cls=Phone_parse))
# print(json.dumps(test_json, default=parse, indent=4))


dic = {
        "person": {
            "name": "Jackie",
            "age": 18,
            "height": 180,
            "dog": [
                {
                    "name": "heihei",
                    "age": 10,
                    "eat": "meat",
                    "isVIP": True
                },
                {
                    "name": "maomao",
                    "age": 5,
                    "eat": "milk"
                }
            ]
        }
    }


# result = jsonpath(dic, "$.person.dog[0].eat")
# result = jsonpath(dic, "$..dog[?(@.isVIP)]")
# result = jsonpath(dic, "$..dog[?(@.age > 5)]")
# result = jsonpath(dic, "$..dog[*].eat")
# print(result)


# import xml.etree.ElementTree as ET
#
# with open("test.xml", "r") as f:
#     result = ET.XML(f.read())
#     print(result)
#
# result = ET.parse("test.xml")
# print(result.findall("student"))
#
# ite = result.iter()
# print(ite)
#
# for it in ite:
#     print(it.attrib)


def sum(n, count):
    result = 0
    while count > 0:
        result += n * 3
        n = n + 5
        count = count -1

    print(result)

sum(35, 35)