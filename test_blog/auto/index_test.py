import unittest
from selenium import webdriver
from auto.HTMLTestRunner import HTMLTestRunner
import re
import time

class Index(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.jiafanblog.com")
        self.default = self.driver.current_window_handle

    def test_index_title(self):
        # 博文标题
        self.driver.find_element_by_xpath('//div[2]/div[2]/div/div[1]/h3/a').click()
        url = self.driver.current_url

    def test_index_free(self):
        try:
            # 个人感悟
            self.driver.find_element_by_xpath('//div[2]/div[2]/div/div[1]/div/div[2]/a').click()
            self.assertNotEqual(self.driver.current_url, "http://www.jiafanblog.com/")
        except Exception as e:
            self.driver.save_screenshot('./image/test_index_free.png')
            raise AssertionError("没有跳转到分类")
            # print("没有跳转到分类")

    def test_index_info(self):
        # 跳转个人页面
        try:
            # 个人感悟
            self.driver.find_element_by_xpath('//div[2]/div/div[1]/div/div[1]/div/div[1]/div/a').click()
            self.assertEqual(self.driver.current_url, "http://www.jiafanblog.com/about")
        except Exception as e:
            self.driver.save_screenshot('./image/test_index_info.png')
            raise AssertionError("没有跳转到个人页面")

    def test_index_image(self):
        try:
            # 通过图片跳转详情页
            src = self.driver.find_element_by_xpath('//div[2]/div[1]/div/div[2]/a/img')
            src_vlaue = src.get_attribute("src")
            src.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            skip_src = self.driver.find_element_by_xpath('//*[@id="waypoint"]/div/div[2]/img')


            skip_src_value = skip_src.get_attribute("src")
            self.assertEqual(src_vlaue, skip_src_value)

            self.driver.switch_to.window(self.default)
        except Exception as e:
            self.driver.save_screenshot('./image/test_index_image.png')
            self.driver.switch_to.window(self.default)
            raise AssertionError("跳转到详情页错误")

    def test_index_category(self):
        # category_个人感悟

        category_list= self.driver.find_elements_by_xpath('//div[2]/div[1]/div[2]/div/a/span')
        for i in range(0, len(category_list)):
            try:
                self.driver.find_element_by_xpath('//div[2]/div[1]/div[2]/div/a[{}]/span'.format(i+1)).click()
                self.driver.switch_to.window(self.driver.window_handles[i+1])
                url = re.match(r"http://www.jiafanblog.com/types/\d*", self.driver.current_url)
                if url:
                    self.assertEqual(self.driver.current_url, url.group())
                self.driver.switch_to.window(self.default)
            except Exception as e:

                self.driver.save_screenshot('./image/test_index_category.png')
                self.driver.switch_to.window(self.default)
                raise AssertionError("没有跳转到分类")

    def test_index_essaycount(self):
        try:
            essay = self.driver.find_elements_by_xpath('//div/div/div[1]/h3/a')
            count = self.driver.find_element_by_css_selector('.m-inline-block').text
            self.assertEqual(len(essay), int(count))
        except Exception as e:
            self.driver.save_screenshot('./image/test_index_essaycount.png')
            raise AssertionError("文章条数统计有误")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
