import unittest

from auto.HTMLTestRunner import HTMLTestRunner
from auto.index_test import Index

if __name__ == '__main__':
    # unittest.main()
    test_suite = unittest.TestSuite()#创建一个测试集合
    test_suite.addTest(Index('test_index_category'))#测试套件中添加测试用例
    #test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    with open('./res.html','wb') as f:
       #打开一个保存结果的html文件
        runner = HTMLTestRunner(stream=f, title='api测试报告', description='测试情况')
        #生成执行用例的对象
        runner.run(test_suite)