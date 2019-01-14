import json
import logging
import requests
from requests.exceptions import MissingSchema, InvalidURL


class Menstent():
    def __init__(self):
        self.session = requests.session()

    def request_get(self, url, session=False, *args, **kwargs):
        try:
            if session:
                response = self.session.get(url, *args, **kwargs)
            else:
                response = requests.get(url, *args, **kwargs)
        except (MissingSchema, InvalidURL):
            logging.error('请检查url = %s 的正确性' % url)
        except ConnectionError:
            logging.error('请检查网络连接情况与api响应时间')
        else:
            return json.dumps(response, indent=2)

    def request_post(self, url, session=False,  *args, **kwargs):
        try:
            if session:
                response = self.session.post(url, *args, **kwargs)
            else:
                response = requests.post(url, *args, **kwargs)
        except (MissingSchema, InvalidURL):
            logging.error('请检查url = %s 的正确性' % url)
        except ConnectionError:
            logging.error('请检查网络连接情况与api响应时间')
        else:
            return json.dumps(response, indent=2)

    def request_put(self, url, session=False,  *args, **kwargs):
        try:
            if session:
                response = self.session.put(url, *args, **kwargs)
            else:
                response = requests.put(url, *args, **kwargs)
        except (MissingSchema, InvalidURL):
            logging.error('请检查url = %s 的正确性' % url)
        except ConnectionError:
            logging.error('请检查网络连接情况与api响应时间')
        else:
            return json.dumps(response, indent=2)

    def request_delete(self, url, session=False,  *args, **kwargs):
        try:
            if session:
                response = self.session.delete(url, *args, **kwargs)
            else:
                response = requests.delete(url, *args, **kwargs)
        except (MissingSchema, InvalidURL):
            logging.error('请检查url = %s 的正确性' % url)
        except ConnectionError:
            logging.error('请检查网络连接情况与api响应时间')
        else:
            return json.dumps(response, indent=2)

    def run_man(self, url, rev_method, *args, **kwargs):
        method =rev_method.lower()
        res = None
        if method == "get":
            res = self.request_get(url, *args, **kwargs)
        elif method == "post":
            res = self.request_post(url, *args, **kwargs)
        elif method == "put":
            res = self.request_put(url, *args, **kwargs)
        elif method == "delete":
            res = self.request_delete(url, *args, **kwargs)
        return res


if __name__ == '__main__':
    # m = Menstent()
    # m.run_man('GET', 'https://www.baidu.com')

    # data = {"data": [{"dep_id": "T09", "dep_name": "Test学院", "master_name": "Test-Master", "slogan": "Here is Slogan"}]}
    # da = Menstent('POST','http://127.0.0.1:8000/api/departments/', data=data).res
    # print(da)

    # r = requests.get('http://www.baidu.com')
    # cookie = requests.utils.dict_from_cookiejar(r.cookies)
    # print(cookie)

    # r = requests.get('https://www.baidu.com', cookies={'BDORZ': '27315'})
    #
    # print(r.text)
    url1 = "http://httpbin.org/cookies/set/sessioncookie/123456789"
    host = "http://httpbin.org/cookies"
    r1 = requests.get(host)
    print(r1.text)

    s = requests.session()
    s.get(url1)
    r = s.get(host)
    print(r.text)