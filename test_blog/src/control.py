import unittest
from selenium import webdriver
from .config.conn import ConnMysql
import re

class Index_control():
    def __init__(self,driver,conn):
        self.driver = driver
        self.conn = conn

    def get_path(self, name):
        # 博文标题
        title = self.conn.select(name)
        print(title)
        return self.driver.find_element_by_xpath(title[0])


    def tearDown(self):
        self.driver.quit()
