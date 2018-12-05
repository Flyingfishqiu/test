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


if __name__ == '__main__':
    p = Pares().test_info()
