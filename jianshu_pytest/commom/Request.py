import json
import logging
import requests
from requests.exceptions import MissingSchema, InvalidURL
from log.log import user_log


class Menstent():
    def __init__(self):
        self.session = requests.session()

    def request_get(self, url, session=False, params=None, *args, **kwargs):
        try:
            if session:
                response = self.session.get(url, params, *args, **kwargs).json()
            else:
                response = requests.get(url, params=params, *args, **kwargs)
                print(response.url)
        except (MissingSchema, InvalidURL):
            logging.error('请检查url = %s 的正确性' % url)
        except ConnectionError:
            logging.error('请检查网络连接情况与api响应时间')
        else:
            return json.dumps(response.json(), indent=2)

    def request_post(self, url, json=None, session=False,  *args, **kwargs):
        try:
            if session:
                response = self.session.post(url, json=json, *args, **kwargs).json()
            else:
                response = requests.post(url, json=json, *args, **kwargs).json()
        except (MissingSchema, InvalidURL):
            logging.error('请检查url = %s 的正确性' % url)
        except ConnectionError:
            logging.error('请检查网络连接情况与api响应时间')
        else:
            return json.dumps(response, indent=2)

    def request_put(self, url, params=None, session=False,  *args, **kwargs):
        try:
            if session:
                response = self.session.put(url, json=params, *args, **kwargs).json()
            else:
                response = requests.put(url, json=params, *args, **kwargs).json()
        except (MissingSchema, InvalidURL):
            logging.error('请检查url = %s 的正确性' % url)
        except ConnectionError:
            logging.error('请检查网络连接情况与api响应时间')
        else:
            return json.dumps(response, indent=2)

    def request_delete(self, url, session=False,  *args, **kwargs):
        try:
            if session:
                response = self.session.delete(url, *args, **kwargs).json()
            else:
                response = requests.delete(url, *args, **kwargs).json()
        except (MissingSchema, InvalidURL):
            logging.error('请检查url = %s 的正确性' % url)
        except ConnectionError:
            logging.error('请检查网络连接情况与api响应时间')
        else:
            return json.dumps(response, indent=2)

    def run_man(self, url, rev_method,  params=None, *args, **kwargs):
        method =rev_method.lower()
        res = None
        if method == "get":
            res = self.request_get(url, params=params, *args, **kwargs)
        elif method == "post":
            res = self.request_post(url,json=params, *args, **kwargs)
        elif method == "put":
            res = self.request_put(url, params=params, *args, **kwargs)
        elif method == "delete":
            res = self.request_delete(url, *args, **kwargs)
        return res


if __name__ == '__main__':
    m = Menstent()
    r = m.run_man('http://127.0.0.1:8000/api/departments/', 'GET')
    print(r)
    user_log.debug('hhhhhh')

    # data = {"data": [{"dep_id": "T09", "dep_name": "Test学院", "master_name": "Test-Master", "slogan": "Here is Slogan"}]}


