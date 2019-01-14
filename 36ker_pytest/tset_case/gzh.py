import time
import unittest

from selenium import webdriver

driver = webdriver.Chrome()

# driver.get('https://mp.weixin.qq.com/s?src=11&timestamp=1547087524&ver=1317&signature=loGDM96u8IomegQaeO0ISDWPKMNrjVufL4v2lkL9mbEgMHO4mja-xD1x-1Ow588CeP96YJoxIX6F1sySSBf5AOA7-Tf6FIvX-Viy5Bk0hv6t7UBHezFcD34DW18nyZRN&new=1')
driver.get('https://mp.weixin.qq.com/s?__biz=MzU2MTE1NDk2Mg==&mid=2247491582&idx=1&sn=3d2d17f826b1a1f86c30d77a2780a43e&chksm=fc7c4103cb0bc8156272185096099dcff7ad32057a635fdc1f15426b90f369d5cb26f01bef5e#rd')
titile = driver.find_element_by_id("activity-name").text

# content = driver.find_element_by_xpath('//*[@id="js_content"]/section[2]/section/section/section[1]').text
# content = driver.find_element_by_xpath('//*[@id="js_content"]/p').text
# time.sleep(3)
content = driver.find_element_by_css_selector('#js_content > p:nth-child(15)').text
print(titile)

# #js_content > p:nth-child(15)
print("--------------------")
print(content)
