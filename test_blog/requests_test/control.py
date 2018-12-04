class Index_control(object):
    def __init__(self, driver, conn):
        self.driver = driver
        self.conn = conn

    def get_path(self, name):
        # 博文标题
        title = self.conn.select(name)
        print(title)
        return self.driver.find_element_by_xpath(title[0])

    def click_element(self, name):
        return self.get_path(name).click()

    def change_window(self, window):
        return self.driver.switch_to.window(window)

    def get_text(self,name):
        return self.get_path(name).text

    def tearDown(self):
        self.driver.quit()
