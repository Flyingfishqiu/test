import unittest
import time
from comment.HTMLTestRunner import HTMLTestRunner
from test_case.login_case_02 import LoginTest


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoginTest))
    file = './report/' + time.strftime("%Y-%m-%d %H_%M_%S") + 'report.html'
    with open(file, 'wb') as f:
        htmlrun = HTMLTestRunner(stream=f, title='36ker 登陆', description='v')
        htmlrun.run(suite)