from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.cnblogs.com/")

# time.sleep(3)
# driver.find_element_by_id('input1').send_keys('小飞鱼q')
# driver.find_element_by_id('input2').send_keys('0929qsj@@@')
# driver.find_element_by_id('remember_me').click()
# driver.find_element_by_id('signin').click()
# u'expiry': 1491887887,
#             u'path': u'/',
#             u'httpOnly': True,
#             u'secure': False
print(driver.get_cookies())
cookie_1 = {
        u"domain": u'.cnblogs.com',
        u"name": u".CNBlogsCookie",
        u"value": u"ABE9AE9CCCEA68FEF58243F39B48DC6AC4A8933AD94F9A01401A78A3C23706D4252D75720A9A5D5FE70AFF1DAEE3A53D15775F981E2939BE720B15D3AB08FA35D79D701FE78CDA1986EC68131D3A0B3B8764F5C9",
        u"expiry": 1491887887,
        u"path": u'/',
        u"httpOnly": True,
        u"secure": False
          }

cookie_2 = {
    u"domain": u".cnbogs.com",
    u'name': u'.Cnblogs.AspNetCore.Cookies',
    u'value': u"CfDJ8KlpyPucjmhMuZTmH8oiYTNVlOIYnQbyVRkCjc8gtQSuW13hpegJYTI2Y5kxm0smWs3XK1NlvbmhQrYEznb9maqEh4wJOO35SnmKa8jrOtfkRGUmM2FSxR2jH6OGdP00krDP4Ydnb5u4X4HPVwWTW_Sh_S8DOVh9OwnH-EU40kj23U9dcsMqAfwb1zRm0aO16QWL1OW0WPJbsTY0BC6Aqwng9ixMFHTVD6QElBhHjyluB8GPIlaoIiaGIV2hSM5wJGZ1BMo8ErQQYsXqm4h4K1h8j55D0CynGLNeprh3BLqGqsYwe5lYK933AmNtYCFkvg",
    u"expiry": 1491887887,
    u"path": u'/',
    u"httpOnly": True,
    u"secure": False
}
driver.add_cookie(cookie_1)
driver.add_cookie(cookie_2)
time.sleep(3)
driver.refresh()
#
# alert = EC.alert_is_present()(driver)
# alert.accept()
# alert = driver.switch_to.alert
# alert.accept()
# alert.dismiss()



"""
    首先 要有明确的分层结构，
    例如 用例、数据、报告、公共的方法 、以及一些配置信息，
    每个模块之间有自己的基本page_obj,可以抽取一个公共的page 类 用来复用，每个用例没有依赖 。
    数据模块中的子模块用来读取 每个 个 页面模块的数据。
    一些公共的工具提取出来。避免代码重复。
    配置信息的话 可以 用来存放 一些静态的变量
    可以通过一个 文件 就可以直接运行 整套流程 ，生成测试报告 ，
    在通过 工具 用来 一键构建
"""