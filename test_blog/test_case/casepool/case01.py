import unittest
from auto.HTMLTestRunner import HTMLTestRunner
from test_case.config.control import Index_control
from selenium import webdriver
from config.conn import ConnMysql
from test_case.pares.read_case import read_case
from test_case.pares.pars_case import Pares


class Index(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        read = read_case()
        self.parse = Pares(read)
        self.base_url = self.parse.get_url()
        self.driver.get(self.base_url)
        self.default = self.driver.current_window_handle
        self.conn = ConnMysql('root', 'q123456')
        self.control = Index_control(self.driver, self.conn)

    def test_index_title(self):
        info = self.parse.get_test_info('test_index_title')
        self.control.click_element(info["xpath_name"])

    def test_index_free(self):
        info = self.parse.get_test_info('test_index_free')
        xpath_name = info["xpath_name"]
        image_url = info["image_url"]
        err_msg = info["err_msg"]
        print(info)
        try:
            # 个人感悟
            self.control.click_element(xpath_name)
            self.assertNotEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot(image_url)
            raise AssertionError(err_msg)

    def test_index_info(self):
        info = self.parse.get_test_info('test_index_info')
        xpath_name = info["xpath_name"]
        image_url = info["image_url"]
        err_msg = info["err_msg"]
        print(info)
        # 跳转个人页面
        try:
            self.control.click_element(xpath_name)
            self.assertEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot(image_url)
            raise AssertionError(err_msg)

    def test_index_image(self):
        info = self.parse.get_test_info('test_index_image')
        xpath_name = info["xpath_name"]
        image_url = info["image_url"]
        err_msg = info["err_msg"]
        print(info)
        try:
            # 通过图片跳转详情页
            src = self.control.get_path(xpath_name)
            src_vlaue = src.get_attribute("src")
            self.control.click_element(xpath_name)
            self.control.change_window(self.driver.window_handles[1])
            skip_src = self.control.get_path("end_image_deftails")
            skip_src_value = skip_src.get_attribute("src")
            self.assertEqual(src_vlaue, skip_src_value)
            self.control.change_window(self.default)

        except Exception as e:
            self.driver.save_screenshot(image_url)
            self.driver.switch_to.window(self.default)
            raise AssertionError(err_msg)

    def test_index_essaycount(self):
        info = self.parse.get_test_info('test_index_essaycount')
        xpath_name = info["xpath_name"]
        image_url = info["image_url"]
        err_msg = info["err_msg"]
        print(info)
        try:
            essay = self.control.get_path("end_image_deftails")
            count = self.control.get_text(xpath_name)
            self.assertEqual(len(essay), int(count))
        except Exception as e:
            self.driver.save_screenshot(image_url)
            raise AssertionError(err_msg)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

