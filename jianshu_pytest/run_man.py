import os
import unittest

from HTMLTestRunner import HTMLTestRunner

from Test_case.test_au import My_test


if __name__ == '__main__':
    files = os.getcwd() + '/reprot/report.html'
    print(files)
    with open(files, 'wb') as f:
        suite = unittest.makeSuite(My_test)
        runner = HTMLTestRunner(stream=f, title='ｌｏｖｅ　＿　林凡')
        runner.run(suite)
