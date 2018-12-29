import time
import unittest
from ddt import ddt, data, unpack
from test_case.models.screenshots import save_image
from test_case.page_obj.loginPage import Login
from .models.myunit import MyTest


@ddt
class LoginTest(MyTest):

    def login_verify(self, username='', password=''):
        Login(self.driver).login(username=username, password=password)

    @data(('', ''), ('', 'linfan520aiai'), ('16619847697', ''))
    @unpack
    def test_login6(self, *args, **kwargs):
        """用户名 密码 都正确"""
        #     # , ('1661984769', 'linfan520aiai'),('16619847697', 'linfan520ai'), ('16619847697', 'linfan520aiai')
        self.login_verify(*args)
        if args[0] == '' and args[1] == '':
            self.assertEqual(Login(self.driver).login_error(), '请输入账户名')
            save_image(self.driver, 'user_pwd_empty.jpg')

        if args[0] == '':
            self.assertEqual(Login(self.driver).login_error(), '请输入账户名')
            save_image(self.driver, 'user_empty.jpg')

        if args[1] == '':
            self.assertEqual(Login(self.driver).login_error(), '请输入验证码')
            save_image(self.driver, 'pwd_empty.jpg')

    def test(self):
        self.login_verify(username='16619847694', password='linfan520aiai')

        lo = Login(self.driver)
        self.assertEqual(lo.login_error(), '用户名或密码错误')
        time.sleep(1)
        save_image(self.driver, 'user_error.jpg')


if __name__ == '__main__':
    unittest.main()