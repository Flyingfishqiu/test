import unittest

from selenium import webdriver

from auto.HTMLTestRunner import HTMLTestRunner


class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://ww.baidu.com")
        self.default = self.driver.current_window_handle

    def test_index_free2(self):
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.save_screenshot("./baidu.png")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Mytest("test_index_free2"))
    # suite.addTest(unittest.makeSuite(Mytest))
    # 执行测试
    with open('./demo.html', 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='博客测试')
        runner.run(suite)