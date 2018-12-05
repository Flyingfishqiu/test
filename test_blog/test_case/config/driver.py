from selenium import webdriver
import time

class Driver(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def get_diver(self, url):
        return self.driver.get(url)


    def __del__(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    d = Driver().get_diver("https://www.baidu.com")