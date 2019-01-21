import json


class Operation_Json(object):
    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = "F:\\测试\\project\\jianshu\\data\\login.json"
        self.data = self.get_data()

    def get_data(self):
        with open(self.file_path) as f:
            data = json.load(f)
            return data

    def get_value(self, value):
        return self.data[value]


if __name__ == '__main__':
    file_path = "../data/login.json"
    openjson = Operation_Json(file_path)
    print(openjson.get_value('login2'))