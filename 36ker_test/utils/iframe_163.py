import time
from selenium import webdriver

def get_driver():
    driver = webdriver.Chrome()
    driver.get('https://mail.163.com/')
    driver.implicitly_wait(5)
    return driver


def tset_163_iframe():
    """
        driver.switch_to.iframe("iframe 的 id 或者 name 或者 元素") : 切换到指定的iframe
        driver.switch_to.default_content() : 切换回Top Windows
    :return:
    """
    driver = get_driver()
    el = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
    driver.switch_to.frame(el)
    driver.find_element_by_class_name('dlemail').send_keys('12221')
    driver.find_element_by_name('password').send_keys('1111111')
    driver.find_element_by_id('dologin').click()
    driver.switch_to.default_content()
    driver.find_element_by_xpath('//*[@id="theme"]/a').click()


def test_window():
    """
        driver.window_handles() : 获取所有的句柄
        driver.curret_window_handle() : 获取当前句柄
        driver.switch_to.window("要切换的句柄")
    """
    driver = get_driver()
    driver.find_element_by_xpath('//*[@id="theme"]/a').click()
    handls = driver.window_handles
    print(driver.current_window_handle)
    print(driver.title)
    driver.switch_to.window(handls[-1])
    print(driver.title)
    print(driver.current_window_handle)
    driver.switch_to.window(handls[0])
    print(driver.title)
    print(driver.current_window_handle)


def test_move_to_element():
    pass

if __name__ == '__main__':
    test_window()



