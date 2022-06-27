import unittest
import time
from package.HTMLTestRunner3_New import HTMLTestRunner


class MyTestCase(unittest.TestCase):
    def test_跳转页面(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
