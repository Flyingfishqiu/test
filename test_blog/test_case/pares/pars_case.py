from test_case.pares.read_case import read_case
import time

class Pares(object):
    def __init__(self, data):
        self.data = data
        self.config = self.data[0]["config"]
        self.test = self.data[1::]

    def get_url(self):
        return self.config["base_url"]

    def get_case_name(self):
        return self.config["name"]

    def get_case_variables(self):
        return self.config["variables"]

    def test_info(self):
        return self.test

    def get_test_info(self, test_name ):
        item = {}
        for info in self.test:
            name = info["test"]["name"]
            if name == test_name:
                err_msg = info["test"]["name"]
                item["err_msg"] = err_msg
                image_url = info["test"]["image_url"]
                item["image_url"] = image_url
                xpath_name = info["test"]["xpath_name"]
                item["xpath_name"] = xpath_name
                print(item)
                return item


if __name__ == '__main__':

    # p = Pares(read_case()).get_test_info('test_index_title')

    print(time.strftime("%Y-%m-%d", time.localtime()))