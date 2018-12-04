import unittest
from .control import Index_control
from selenium import webdriver
from config.conn import ConnMysql


class RunCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.jiafanblog.com"
        self.driver.get(self.base_url)
        self.default = self.driver.current_window_handle
        self.conn = ConnMysql('root', 'q123456')
        self.control = Index_control(self.driver, self.conn)

    def parse(self, data):
        for test in data[1::]:
            test = test["test"]
            self.err_msg = test["err_msg"]
            self.image_url = test["image_url"]
            self.xpath_name = test["xpath_name"]
            exec(test["name"]+"()")


    def test_index_title(self):
        self.control.click_element("title")

    def test_index_free(self):
        try:
            # 个人感悟
            self.control.click_element(self.xpath_name)
            self.assertNotEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot(self.image_url)
            raise AssertionError(self.err_msg)

    def test_index_info(self):
        # 跳转个人页面
        try:
            self.control.click_element(self.xpath_name)
            self.assertEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot(self.image_url)
            raise AssertionError(self.err_msg)

    def test_index_image(self):
        try:
            # 通过图片跳转详情页
            src = self.control.get_path("start_image_details")
            src_vlaue = src.get_attribute("src")
            self.control.click_element("start_image_details")
            self.control.change_window(self.driver.window_handles[1])
            skip_src = self.control.get_path("end_image_deftails")
            skip_src_value = skip_src.get_attribute("src")
            self.assertEqual(src_vlaue, skip_src_value)
            self.control.change_window(self.default)

        except Exception as e:
            self.driver.save_screenshot(self.image_url)
            self.driver.switch_to.window(self.default)
            raise AssertionError(self.err_msg)

    def test_index_essaycount(self):
        try:
            essay = self.control.get_path("end_image_deftails")
            count = self.control.get_text("count")
            self.assertEqual(len(essay), int(count))
        except Exception as e:
            self.driver.save_screenshot(self.image_url)
            raise AssertionError(self.err_msg)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

