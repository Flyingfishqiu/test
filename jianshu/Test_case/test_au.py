import unittest
import json
from commom.Request import Menstent
from ddt import ddt, data
from commom.get_data import Get_data
from commom.is_content import is_contents
from commom.operation_excle import OperationExcle


def get_data():
    getdata = Get_data()
    list_data = []
    for i in range(1, getdata.get_case_count()):
        item = {}
        methods = getdata.get_methods(i)
        url = getdata.get_case_Url(i)
        # data = getdata.get_data(i)
        data = getdata.get_case_data(i)
        expect = getdata.get_expect(i)
        item["url"] = url
        item["methods"] = methods
        item["data"] = data
        item["expect"] = expect
        item["i"] = i
        list_data.append(item)
    return list_data




@ddt
class My_test(unittest.TestCase):
    def setUp(self):
        self.run = Menstent()
        self.get_data = Get_data()
        self.excle = OperationExcle()

    @unittest.skip("test_01")
    def test_01(self):
        url = "http://127.0.0.1:8000/api/departments/"
        method = 'GET'
        print("--test_01")
        self.run.run_man(method, url)

    @data(*get_data())
    def test_04(self, item):
        print(item["url"], item["methods"], item["data"], item["expect"], item["i"])
        self.run_test(url=item["url"], methods=item["methods"], params=item["data"], expect=item["expect"], i=item["i"])

    def run_test(self, url, methods, i, params=None, expect=None):
        ret = self.run.run_man(url=url, rev_method=methods, params=params)
        ret2 = str(json.loads(ret))

        if is_contents(expect, ret2):
            self.get_data.write_data(i, 'pass')
        else:
            self.get_data.write_data(i, 'fail')
        self.assertIn(expect, ret2)


if __name__ == '__main__':
    print(get_data())
    # suite = unittest.TestSuite()
    # suite.addTest(My_test('test_02'))
    # unittest.TextTestRunner().run(suite)