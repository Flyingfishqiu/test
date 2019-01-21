import unittest


class Assert_util():

    def __init__(self, test_case=unittest.TestCase):
        self.test_case = test_case

    def assert_Equal(self, first, second, msg=None):
        self.test_case.assertEqual(first, second, msg)

    def assert_True(self,  first, second, msg=None):
        self.test_case.assertTrue(first, second, msg)

    def assert_NotEqual(self, first, second, msg=None):
        self.test_case.assertNotEqual(first, second, msg)

    def assert_False(self, second, msg=None):
        self.test_case.assertFalse(second, msg)


"""


"""

