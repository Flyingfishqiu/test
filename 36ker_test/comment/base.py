from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from driver.driver import mydriver
from selenium.webdriver.support.ui import Select


class Base_Page(object):
    url = 'https://account.36kr.com/'

    def __init__(self, base_driver: webdriver.Chrome,  base_url=url):
        self.driver = base_driver
        self.driver.maximize_window()
        self.base_url = base_url
        self.timeout = 10

    def driver_open(self, url=''):
        self.driver.get(self.base_url+url)

    def findElement(self, element):
        """
        查找符合元素单个值
        :param element:
        :return: element
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element(*element))
        except Exception as e:
            print("%s 页面中未能找到 %s 元素" % (self, element))

    def findElements(self, element):
        """
        查找符合元素的所有值
        :param element:
        :return: element []
        """
        try:
            return WebDriverWait(self.driver, 5).until(lambda x: x.fiand_elements(*element))
        except Exception as e:
            print("%s 页面中未能找到 %s 元素" % (self, element))
            return []

    def send_keys(self, element, value, clear_first=True, click_first=True):
        """
        输入值
        :param element:
        :param value:
        :param clear_first:
        :param click_first:
        :return:
        """
        try:
            if click_first:
                self.findElement(element).click()

            if clear_first:
                self.findElement(element).clear()
            self.findElement(element).send_keys(value)
        except ArithmeticError:
            print("%s 页面中未能找到 %s 元素" % (self, element))

    def move_to(self, element):
        """
        鼠标悬浮
        :param element:
        :return:
        """
        try:
            el = self.findElement(element)
        except TimeoutError:
            print('element not found: %s ' % element)
        else:
            ActionChains(self.driver).move_to_element(el).perform()

    def select_by_value(self, element, value):
        """
       根据value选中下拉列表元素
       :param element:
       :param index:
       :return:
       """
        el = self.findElement(element)
        Select(el).select_by_value(value)

    def select_by_index(self, element, index=0):
        """
        根据下标选中下拉列表元素
        :param element:
        :param index:
        :return:
        """
        el = self.findElement(element)
        Select(el).select_by_index(index)

    def select_by_visible_text(self, element, text):
        """
        根据文本选中下拉列表
        :param element:
        :param text:
        :return:
        """
        el = self.findElement(element)
        Select(el).select_by_visible_text(text)

    def frame_switch(self, element):
        """
        切换iframe
        :param element:
        :return:
        """
        el = self.findElement(element)
        self.driver.switch_to.frame(el)

    def window_swich(self, index=-1):
        """
        切换窗口
        :param index:
        :return:
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])


    def scrol_Top(self):
        """
        回到顶部
        :return:
        """
        js = "window.scrollTo(0,document.body.scrollTop=0)"
        self.driver.execute_script(js)

    def scroll_Food(self):
        """
        滑到底部
        :return:
        """
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def element_text(self, element):
        self.move_to(element)
        return self.findElement(element).text

if __name__ == '__main__':
    b = Base_Page(mydriver())
    b.driver_open()
    new_user = (By.XPATH, "//form/div[1]/a")
    print(b.element_text(new_user))

