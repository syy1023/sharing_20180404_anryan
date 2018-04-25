#coding=utf-8

import unittest
import HTMLTestRunner
class Test(unittest.TestCase):
    def setUp(self):
        print u'开始'

    
    def test_add(self):
        self.assertEqual((1+2), 3)

    def test_multiply(self):
        self.assertFalse('loo'.isupper())
        

    def test_in(self):
        self.assertIn("a" in "aabc")
        

    def test_fail(self):
        self.assertEqual(1, 2, 'not equal')

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    
    testunit.addTest(Test("test_add"))
    testunit.addTest(Test("test_multiply"))
    testunit.addTest(Test("test_in"))
    testunit.addTest(Test("test_fail"))
    

     
    filename="C:\\Users\\test\\Desktop\\sharing\\result2.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='result',description='allcases')
    runner.run(testunit)
    fp.close()
