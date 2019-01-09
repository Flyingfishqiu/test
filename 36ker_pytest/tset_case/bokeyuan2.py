from selenium import webdriver
import time

driver = webdriver.Chrome()
# 启动浏览器后获取cookies
print(driver.get_cookies())
driver.get("http://www.cnblogs.com")
# 打开主页后获取cookies
print( driver.get_cookies())
# 登录后获取cookies
url = "https://passport.cnblogs.com/user/signin"
driver.get(url)
driver.implicitly_wait(30)
driver.find_element_by_id("input1").send_keys(u"小飞鱼q")
driver.find_element_by_id("input2").send_keys(u"0929qsj@@@")
driver.find_element_by_id("signin").click()
time.sleep(3)
print(driver.get_cookies())

# 获取指定name的cookie
print(driver.get_cookie(name=".CNBlogsCookie"))

# 清除指定name的cookie
driver.delete_cookie(name=".CNBlogsCookie")
print(driver.get_cookies())
# 为了验证此cookie是登录的，可以删除后刷新页面
driver.refresh()

# 清除所有的cookie
driver.delete_all_cookies()
print(driver.get_cookies())

