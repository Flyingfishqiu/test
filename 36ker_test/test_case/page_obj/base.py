from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver.driver import mydriver


class Base_Page(object):
    url = 'https://account.36kr.com/'

    def __init__(self, base_driver,  base_url=url):
        self.driver = base_driver
        self.base_url = base_url

    def driver_open(self, url=''):
        self.driver.get(self.base_url+url)

    def find_element(self, *element):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(element))
            return self.driver.find_element(*element)
        except Exception as e:
            print("%s 页面中未能找到 %s 元素" % (self, element))

    def find_elements(self, *element):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(element))
            return self.driver.find_elements(*element)
        except Exception as e:
            print("%s 页面中未能找到 %s 元素" % (self, element))

    def swtich_frame(self, element):
        return self.driver.switch_to.frame(element)

    def send_keys(self, element, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(*element).click()

            if clear_first:
                self.find_element(*element).clear()
            self.find_element(*element).send_keys(value)
        except ArithmeticError:
            print("%s 页面中未能找到 %s 元素" % (self, element))


if __name__ == '__main__':
    b = Base_Page(mydriver())
    b.driver_open()
