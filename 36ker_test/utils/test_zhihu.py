import time
import unittest
from selenium import webdriver
import json

class Test_zhihu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        url = "https://www.zhihu.com/"
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    # def test_01(self):
    #     # pass
    #     # Popover1 - toggle
    #     self.driver.find_element_by_css_selector(".Popover1-toggle").send_keys('python')
    #     try:
    #         el = self.driver.find_element_by_css_selector("//div[@class='SearchBar']/button[text()='提问']")
    #         el.click()
    #     except:
    #         print("没有找到提问按钮")


    def save_cookie(self, cookie):

        with open('cooke.json', 'w') as f:
            f.write(json.dumps(cookie))

    def test_02(self):

        self.driver.find_element_by_xpath("//span[text()='登录']").click()
        time.sleep(2)
        name = self.driver.find_element_by_name('username')
        name.send_keys('6619847697')
        print(name.is_displayed())
        print(self.driver.title)
        print(name.get_attribute('class'))
        self.driver.find_element_by_name('password').send_keys('linfan520aiai')
        time.sleep(6)
        butt = self.driver.find_element_by_xpath('//button[@type="submit"]')
        print(butt)
        butt.click()

        print(self.driver.name)

