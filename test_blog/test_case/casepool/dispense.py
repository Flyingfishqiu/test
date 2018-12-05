from auto.HTMLTestRunner import HTMLTestRunner
from test_case.config.test_parse import ParametrizedTestCase
from test_case.pares.read_case import read_case
from test_case.pares.pars_case import Pares
import importlib
import unittest


class Dispense(object):
    def __init__(self):
        self.parse = Pares(read_case())

    def dispense_test_model(self):
        name = self.parse.get_case_name()
        path = "test_case.casepool."+name
        model = importlib.import_module(path)
        return model

    def get_url(self):
        return self.parse.get_url()

    def dispense_parse(self):

        for info in self.parse.test_info():

            name = info["test"]["name"]
            err_msg = info["test"]["name"]
            image_url = info["test"]["image_url"]
            xpath_name = info["test"]["xpath_name"]
            model = self.dispense_test_model()
            index = getattr(model, "Index")
            # getattr(index, name)(xpath_name, image_url, err_msg)
            index().setUp()
            # suite = unittest.TestSuite()
            # suite.addTest(index(name, xpath_name=xpath_name, image_url=image_url,
            #                                                err_msg=err_msg))
            suite = ParametrizedTestCase.parametrize(index, name, xpath_name=xpath_name, image_url=image_url, err_msg=err_msg)

            with open('../report/demo.html', 'wb') as f:
                runner = HTMLTestRunner(f, verbosity=2, title='博客测试')
                runner.run(suite)

    def run_case(self):
       pass




if __name__ == '__main__':
    d = Dispense().dispense_parse()
    # unittest.main()

