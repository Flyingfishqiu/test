from selenium.webdriver.common.by import By
from comment.base import Base_Page


class Index_Page(Base_Page):
    avatar_image_element = (By.CLASS_NAME, 'head-avatar-img')
    select_element = (By.CLASS_NAME, 'headericon-Icon_Search')
    select_element2 = (By.CLASS_NAME, 'J_searchInput')

    def avatar_image(self):
        self.move_to(*self.avatar_image_element)

    def click_select(self):
        self.find_element(*self.select_element).click()

    def send_select(self):
        self.send_keys(*self.select_element2)

#
