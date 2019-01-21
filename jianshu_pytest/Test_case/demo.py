from lxml import etree
import requests

from Test_case.test_au import Test_jiekou
from Test_case.test_au import get_data
from commom.Request import Menstent


def get_xapth():
    headers = {

        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"

    }
    r = requests.get('https://mifengcha.com/ico/honeybox', headers=headers)
    html = etree.HTML(r.content.decode("utf-8"))
    result = html.xpath('//section[@class="mgt50"]/ul/li')
    item = {}
    for i, li in enumerate(result):
        if i <= 1:
            value = li.xpath("./text()")
            name = li.xpath("./span[1]/text()")
            item[name[0].split(" :")[0].strip()] = value[0].split(" :")[0].strip()
        else:
            span = li.xpath("./span[1]/text()")
            span2 = li.xpath("./span[2]//text()")
            mytest = [i for i in span2 if i != ' ']
            item[span[0].split(" :")[0].strip("：")] = mytest[0].strip()
    return item


if __name__ == '__main__':
    pass
    # url = "http://127.0.0.1:8000/api/departments/"
    # methods = "GET"
    # m = Menstent()
    # print(m.run_man(url=url, rev_method=methods))
    # My_test().run_test(url=url, methods=methods, expect="T05", i=4)