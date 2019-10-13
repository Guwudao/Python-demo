import requests

url = "http://openapi.tuling123.com/openapi/api/v2"

parameter_json = {
                    "reqType":0,
                    "perception": {
                        "inputText": {
                            "text": "你是谁??"
                        }
                    },
                    "userInfo": {
                        "apiKey": "0e4dc4f3608b4da38dbbac4c746b6428",
                        "userId": "single"
                    }
                }

response = requests.post(url, json=parameter_json)

print(response.json())