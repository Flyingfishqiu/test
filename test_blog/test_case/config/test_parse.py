import unittest


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, name, **kwargs):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        suite = unittest.TestSuite()
        suite.addTest(testcase_klass(name, param=kwargs))
        return suite
