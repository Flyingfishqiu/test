import time
from selenium.webdriver.common.by import By
from driver.driver import mydriver
from comment.base import Base_Page


class Login(Base_Page):
    username_element = (By.ID, 'kr-shield-username')
    password_element = (By.ID, 'kr-shield-password')
    submit_element = (By.ID, 'kr-shield-submit')
    error_msg_element = (By.XPATH, '//form/div[2]/div/span')
    login_success_element = (By.XPATH, '/html/body/header/div[2]/div[3]/ul/li[4]/a/div')
    # move_to_avatar = (By.CLASS_NAME, 'head-avatar-img')
    move_to_avater = (By.XPATH, '//ul/li[4]/a/div')
    success_user_name = (By.XPATH, '//li[4]/div/a/span')

    def username(self, username):
        self.send_keys(self.username_element, username)

    def password(self, password):
        self.send_keys(self.password_element, password)

    def submit(self):
        self.findElement(self.submit_element).click()

    def login(self, username, password):
        self.driver_open('?ok_url=https%3A%2F%2F36kr.com%2F#/login?pos=header')
        self.username(username)
        self.password(password)
        self.submit()
        self.driver.delete_all_cookies()
        time.sleep(2)

    def login_error(self, expect):
        if expect:
            self.move_to(self.move_to_avater)
            return self.element_text(self.success_user_name)
        else:
            return self.findElement(self.error_msg_element).text

    def login_success(self):
        self.move_to(self.move_to_avater)
        return self.element_text(self.success_user_name)

if __name__ == '__main__':
    l = Login(mydriver())
    # l.driver_open()
    # l.username('16619847697')
    l.login('16619847697', 'linfan520aiai')
    print(l.login_success())