import unittest
import ddt
from comment.screenshots import save_image
from page_obj.loginPage import Login
from comment.myunit import MyTest
from data.Excel_data import ExcelUti

e = ExcelUti('E:\\frame\\测试\\test\\36ker_test\\data\execl\\login.xlsx', 'Sheet1')
login_data = e.get_data()

@ddt.ddt
class LoginTest(MyTest):

    def login_verify(self, username='', password=''):
        Login(self.driver).login(username=username, password=password)

    def Login_ker(self, username, password, msg, expect, image):
        self.login_verify(username=username, password=password)
        self.assertEqual(Login(self.driver).login_error(expect), msg)
        save_image(self.driver, image+'.jpg')

    @ddt.data(*login_data)
    def test_login_01(self, da):
        self.Login_ker(da['username'], da['password'], da['error_msg'], da["expect"], da['image'])


if __name__ == '__main__':
    unittest.main()
