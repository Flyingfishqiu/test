import unittest
from .control import Index_control
from selenium import webdriver
from config.conn import ConnMysql


class Index(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.jiafanblog.com"
        self.driver.get(self.base_url)
        self.default = self.driver.current_window_handle
        self.conn = ConnMysql('root', 'q123456')
        self.control = Index_control(self.driver, self.conn)

    def test_index_title(self):
        self.control.click_element("title")

    def test_index_free(self):
        try:
            # 个人感悟
            self.control.click_element("free")
            self.assertNotEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot('./image/test_index_free.png')
            raise AssertionError("没有跳转到分类")

    def test_index_info(self):
        # 跳转个人页面
        try:
            self.control.click_element("user_info")
            self.assertEqual(self.driver.current_url, self.base_url)
        except Exception as e:
            self.driver.save_screenshot('./image/test_index_info.png')
            raise AssertionError("没有跳转到个人页面")

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
            self.driver.save_screenshot('./image/test_index_image.png')
            self.driver.switch_to.window(self.default)
            raise AssertionError("跳转到详情页错误")

    def test_index_essaycount(self):
        try:
            essay = self.control.get_path("end_image_deftails")
            count = self.control.get_text("count")
            self.assertEqual(len(essay), int(count))
        except Exception as e:
            self.driver.save_screenshot('./image/test_index_essaycount.png')
            raise AssertionError("文章条数统计有误")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

