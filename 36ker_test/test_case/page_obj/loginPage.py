import time
from selenium.webdriver.common.by import By
from driver.driver import mydriver
from test_case.page_obj.base import Base_Page


class Login(Base_Page):
    username_element = (By.ID, 'kr-shield-username')
    password_element = (By.ID, 'kr-shield-password')
    submit_element = (By.ID, 'kr-shield-submit')
    error_msg_element = (By.XPATH, '//form/div[2]/div/span')
    login_success_element = (By.XPATH, '/html/body/header/div[2]/div[3]/ul/li[4]/a/div')

    def username(self, username):
        self.send_keys(self.username_element, username)

    def password(self, password):
        self.send_keys(self.password_element, password)

    def submit(self):
        self.find_element(*self.submit_element).click()

    def login(self, username, password):
        self.driver_open('?ok_url=https%3A%2F%2F36kr.com%2F#/login?pos=header')
        self.username(username)
        self.password(password)
        self.submit()
        time.sleep(2)

    def login_error(self):
        return self.find_element(*self.error_msg_element).text

    def login_success(self):
        return self.find_element(*self.login_success_element)


if __name__ == '__main__':
    l = Login(mydriver())
    l.driver_open()
    l.username('16619847697')