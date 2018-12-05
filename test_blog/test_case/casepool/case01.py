import unittest
from auto.HTMLTestRunner import HTMLTestRunner
from test_case.config.control import Index_control
from selenium import webdriver
from config.conn import ConnMysql
from test_case.casepool.dispense import Dispense
from test_case.config.test_parse import ParametrizedTestCase


class Index(ParametrizedTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.dispense = Dispense()
        self.base_url = self.dispense.get_url()
        self.driver.get(self.base_url)
        self.default = self.driver.current_window_handle
        self.conn = ConnMysql('root', 'q123456')
        self.control = Index_control(self.driver, self.conn)

    def test_index_free2(self):
        try:
            # 个人感悟
            self.control.click_element("free")
            self.assertNotEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot('./image/test_index_free.png')
            raise AssertionError("没有跳转到分类")

    def test_index_title(self, xpath_name, image_url, err_msg):
        print(xpath_name, image_url, err_msg)
        self.control.click_element(xpath_name)

    def test_index_free(self, xpath_name, image_url, err_msg):
        print(xpath_name, image_url, err_msg)
        try:
            # 个人感悟
            self.control.click_element(xpath_name)
            self.assertNotEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot(image_url)
            raise AssertionError(err_msg)

    def test_index_info(self, xpath_name, image_url, err_msg):
        print(xpath_name, image_url, err_msg)
        # 跳转个人页面
        try:
            self.control.click_element(xpath_name)
            self.assertEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot(image_url)
            raise AssertionError(err_msg)

    def test_index_image(self, xpath_name, image_url, err_msg):
        print(xpath_name, image_url, err_msg)
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

    def test_index_essaycount(self, xpath_name, image_url, err_msg):
        print(xpath_name, image_url, err_msg)
        try:
            essay = self.control.get_path("end_image_deftails")
            count = self.control.get_text("count")
            self.assertEqual(len(essay), int(count))
        except Exception as e:
            self.driver.save_screenshot(image_url)
            raise AssertionError(err_msg)

    def __del__(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

