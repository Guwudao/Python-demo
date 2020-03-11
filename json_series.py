import json


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
print(json.dumps(test_json, default=parse, indent=4))