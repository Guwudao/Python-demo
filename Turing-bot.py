import requests


class TuringBot:

    url = "http://openapi.tuling123.com/openapi/api/v2"

    singal_thread = "0e4dc4f3608b4da38dbbac4c746b6428"
    not_robot_key = "07a354c4f9a04feeb3145f9a77a473b1"

    @classmethod
    def automatic_reply(cls, text):

        parameter_json = """{
                            "reqType": 0,
                            "perception": {
                                "inputText": {
                                    "text": %s
                                }
                            },
                            "userInfo": {
                                "apiKey": cls.not_robot_key,
                                "userId": "single"
                            }
                        }""" % text

        response = requests.post(cls.url, json=parameter_json)
        return response.json()["results"][0]["values"]["text"]

