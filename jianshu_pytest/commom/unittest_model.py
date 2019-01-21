import unittest
from Test_case.test_au import My_test
from HTMLTestRunner import HTMLTestRunner

class Unittest_Model(object):
    def __init__(self, rev_suite):
        self.__loader = unittest.TestLoader()
        self.suite = self.make_suite(rev_suite)

    def add_test(self, test):
        return self.suite.addTest(test)

    def load_test_from_model(self, model_name):
        __suite = self.__loader.loadTestsFromModule(module=model_name)
        return __suite

    def load_test_from_case(self, case):
        __suite = self.__loader.loadTestsFromTestCase(testCaseClass=case)
        return __suite

    def load_test_from_name(self, name):
        __suite = self.__loader.loadTestsFromName(name=name)
        return __suite

    def load_test_from_names(self, names):
        __suite = self.__loader.loadTestsFromNames(names=names)
        return __suite

    def make_suite(self, rev_suite):
        suite = unittest.TestSuite(rev_suite)
        return suite

    def run_suite(self, rev_suite, report=False, stream='', verbosity=1, title=None, description=None):

        if report == False:
            unittest.TextTestRunner().run(rev_suite)
        else:
            html_run = HTMLTestRunner(stream=stream, verbosity=verbosity, title=title, description=description)
            html_run.run(rev_suite)


if __name__ == '__main__':
    l = [My_test('test_01'), My_test('test_02')]
    model = Unittest_Model(l)
    su = model.add_test(My_test('test_01'))

