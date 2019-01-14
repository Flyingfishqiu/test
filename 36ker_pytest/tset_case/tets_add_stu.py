import logging

import pytest



# class Test_01(object):

    # 每个用例之前都会执行一次
    # def setup(self):
    #     print('setup-')
    #
    # # 每个用例之后都会执行一次
    # def teardown(self):
    #     print('teardow')
    #
    # # 每个类之前会执行一次
    # def setup_class(self):
    #     print('setup_class')
    #
    # # 每个类结束之后会执行一次
    # def teardown_class(self):
    #     print("teardown_class")

# @pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
# def fix():
#     print('fixture')

def fun( x, y):
    return x + y

def test_01(fix):
    print("---01")
    assert fun(2, 4) > 4

def test_02(fix):
    print("----02")

def test_03(fix):
    print("---03")
    assert fun(2, 4) > 2

def test_04(fix):
    print("---04")
    assert fun(2, 4) > 3