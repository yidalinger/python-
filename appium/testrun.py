import os
import time
import unittest
from bao.HTMLTestRunner3_New import HTMLTestRunner

# unittest.main()
lj = os.getcwd()
testlj = os.path.join(lj, 'bao')

d = unittest.TestLoader().discover(start_dir=lj, pattern='test_1.py')
now = time.strftime('%Y-%m-%d-%H-%M-%S')
bglj = os.path.join(lj, 'ui')

fname = os.path.abspath(os.path.join(bglj, f'ui{str(now)}.html'))

with open(fname, 'wb') as f:
    r = HTMLTestRunner(stream=f, title='app测试', description='测试', tester='朱凯宏')
    r.run(d)
