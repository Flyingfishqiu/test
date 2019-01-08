import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Baidu(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def is_tatile(self):
        print(EC.title_is('百度一下，你就知道')(self.driver))

    def title_contains_baidu(self):
        time.sleep(3)
        print(EC.title_contains('百度')(self.driver))
        # 判断文本
        # print(EC.text_to_be_present_in_element((By.CLASS_NAME, 'mine-text'),  '我的关注')(self.driver))
        # 判断值————value
        print(EC.text_to_be_present_in_element_value((By.ID, "su"), '百度一下')(self.driver))


if __name__ == '__main__':
    baidu = Baidu()
    baidu.title_contains_baidu()