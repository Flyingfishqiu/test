import unittest
from commom.Request import Menstent
from mock import mock


class My_test(unittest.TestCase):
    def setUp(self):
        self.run = Menstent()

    # @unittest.skip("test_01")
    def test_01(self):
        url = "http://127.0.0.1:8000/api/departments/"
        method = 'GET'
        print("--test_01")
        self.run.run_man(method, url)

    # @unittest.skip('test_02')
    def test_02(self):
        data = {
            "data": [{"dep_id": "T09", "dep_name": "Test学院", "master_name": "Test-Master", "slogan": "Here is Slogan"}]}
        method = "POST"
        url = 'http://127.0.0.1:8000/api/departments/'
        print('---test_02')
        self.run.run_man = mock.Mock(return_value=data)
        ret = self.run.run_man(method, url, data=data)
        print(ret)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(My_test('test_02'))
    unittest.TextTestRunner().run(suite)