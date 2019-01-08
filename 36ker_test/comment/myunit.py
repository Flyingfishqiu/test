import unittest

from selenium.webdriver.common.by import By

from driver.driver import mydriver
import time


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = mydriver()

    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # self.driver.get('https://account.36kr.com/?ok_url=https%3A%2F%2F36kr.com%2F#/login?pos=header')

    # def test(self):
    #     print('lalal')

    # def test(self):
    #     username_element = (By.ID, 'kr-shield-username')
    #     password_element = (By.ID, 'kr-shield-password')
    #     self.driver.find_element(*username_element).send_keys('16619847697')
    #     self.driver.find_element(*password_element).send_keys('linfan520ai')
    #     self.driver.find_element(By.ID, 'kr-shield-submit').click()
    #     time.sleep(3)
    #     # login_success_element = (By.XPATH, '//li[4]/div/a/span/text()')
    #     error_msg_element = (By.XPATH, '//form/div[2]/div/span/text()')
    #     # print(self.driver.find_element(*login_success_element))
    #     # print(self.driver.find_element_by_xpath('//form/div[2]/div/span').text)
    #     time.sleep(2)
    #     print(self.driver.find_element(By.XPATH, '//form/div[2]/div/span').text)
    #     # print(self.driver.find_element(By.CLASS_NAME, 'ng-binding'))

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()