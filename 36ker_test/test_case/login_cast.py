import time

from comment.screenshots import save_image
from page_obj.loginPage import Login
from comment.myunit import MyTest
import unittest


class LoginTest(MyTest):

    def login_verify(self, username='', password=''):
        Login(self.driver).login(username=username, password=password)

    # def test_login1(self):
    #     """用户名密码都为空"""
    #     self.login_verify()
    #     self.assertEqual(Login(self.driver).login_error(), '请输入账户名')
    #     save_image(self.driver, 'user_pwd_empty.jpg')
    #
    # def test_login2(self):
    #     """用户名为空"""
    #     self.login_verify(password='linfan520aiai')
    #     self.assertEqual(Login(self.driver).login_error(), '请输入账户名')
    #     save_image(self.driver, 'user_empty.jpg')
    #
    # def test_login3(self):
    #     """密码为空"""
    #     self.login_verify(username='16619847697')
    #     self.assertEqual(Login(self.driver).login_error(), '请输入验证码')
    #     save_image(self.driver, 'pwd_empty.jpg')
    #
    # def test_login4(self):
    #     """用户名错误 密码正确"""
    #     self.login_verify(username='16619847694', password='linfan520aiai')
    #     self.assertEqual(Login(self.driver).login_error(), '用户名或密码错误')
    #     save_image(self.driver, 'user_error.jpg')
    #
    # def test_login5(self):
    #     """用户名正确密码错误"""
    #     self.login_verify(username='16619847694', password='linfan520aiai')
    #     self.assertEqual(Login(self.driver).login_error(), '用户名或密码错误')
    #     save_image(self.driver, 'pwd_error.jpg')

    def test_login6(self):
        """用户名 密码 都正确"""
        self.login_verify(username='16619847697', password='linfan520aiai')
        time.sleep(3)
        name = Login(self.driver).login_success()
        self.assertEqual(name, 'qiusijia')
        save_image(self.driver, 'ok.jpg')


if __name__ == '__main__':
    unittest.main()