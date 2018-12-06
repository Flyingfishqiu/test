from auto.HTMLTestRunner import HTMLTestRunner
from test_case.pares.read_case import read_case
from test_case.pares.pars_case import Pares
import importlib
import unittest
from test_case.casepool.case01 import Index
import time


class Dispense(object):
    def __init__(self):
        self.parse = Pares(read_case())

    def dispense_test_model(self):
        name = self.parse.get_case_name()
        path = "test_case.casepool."+name
        model = importlib.import_module(path)
        return model

    def run_case(self):
        suite = unittest.TestSuite()
        # suite.addTest(Index("test_index_title"))
        suite.addTest(unittest.makeSuite(Index))
        path_time = "../report/"+time.strftime("%Y-%m-%d", time.localtime())+"-博客.html"
        with open(path_time, 'wb') as f:
            runner = HTMLTestRunner(f, verbosity=2, title='博客测试')
            runner.run(suite)


if __name__ == '__main__':
    d = Dispense().run_case()


